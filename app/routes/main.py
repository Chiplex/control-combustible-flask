from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
from decimal import Decimal
from app.models.tanques import Tanques
from app.models.transferencias import Transferencias
from app.models.transacciones import Transacciones
from app.models.responsables import Responsables
from app import db
import uuid

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/registro_combustible', methods=['GET', 'POST'])
def registro_combustible():
    if request.method == 'POST':
        tanque_origen_id = request.form.get('tanque_origen_id')
        tanque_destino_id = request.form.get('tanque_destino_id')
        responsable_id = request.form.get('responsable_id')
        cantidad = Decimal(request.form.get('cantidad'))
        detalles = request.form.get('detalles', '')

        try:
            # Verificar que los tanques existan
            tanque_origen = Tanques.query.filter_by(TanqueId=tanque_origen_id).first()
            tanque_destino = Tanques.query.filter_by(TanqueId=tanque_destino_id).first()
            
            if not tanque_origen or not tanque_destino:
                flash('Error: Tanques no encontrados', 'error')
                return redirect(url_for('main.registro_combustible'))

            # Verificar que el origen sea de almacenamiento y el destino de consumo
            if tanque_origen.tipo != 'Almacenamiento':
                flash('Error: El tanque origen debe ser de tipo Almacenamiento', 'error')
                return redirect(url_for('main.registro_combustible'))
            
            if tanque_destino.tipo != 'Consumo':
                flash('Error: El tanque destino debe ser de tipo Consumo', 'error')
                return redirect(url_for('main.registro_combustible'))

            # Verificar saldo suficiente en tanque origen
            saldo_origen = tanque_origen.Saldo or Decimal('0')
            if saldo_origen < cantidad:
                flash(f'Error: Saldo insuficiente en tanque origen. Saldo actual: {saldo_origen}L, Cantidad solicitada: {cantidad}L', 'error')
                return redirect(url_for('main.registro_combustible'))

            # Crear transacción
            transaccion_id = str(uuid.uuid4())
            nueva_transaccion = Transacciones(
                TransaccionId=transaccion_id,
                Detalles=f"Transferencia de {cantidad}L de {tanque_origen.Codigo} a {tanque_destino.Codigo}",
                UsuarioId='SISTEMA',
                Estado='COMPLETADA'
            )

            # Crear registro de salida
            transferencia_salida = Transferencias(
                TransferenciaId=str(uuid.uuid4()),
                TanqueId=tanque_origen_id,
                ResponsableId=responsable_id,
                RecepcionId=tanque_destino_id,
                Cantidad=-cantidad,  # Cantidad negativa para salida
                Tipo='SALIDA',
                Detalles=f"Salida hacia {tanque_destino.Codigo}: {detalles}",
                FechaTransferencia=datetime.utcnow(),
                TransaccionId=transaccion_id,
                Estado='COMPLETADA',
                UsuarioId='SISTEMA'
            )

            # Crear registro de entrada
            transferencia_entrada = Transferencias(
                TransferenciaId=str(uuid.uuid4()),
                TanqueId=tanque_destino_id,
                ResponsableId=responsable_id,
                RecepcionId=tanque_origen_id,
                Cantidad=cantidad,  # Cantidad positiva para entrada
                Tipo='ENTRADA',
                Detalles=f"Entrada desde {tanque_origen.Codigo}: {detalles}",
                FechaTransferencia=datetime.utcnow(),
                TransaccionId=transaccion_id,
                Estado='COMPLETADA',
                UsuarioId='SISTEMA'
            )

            # Actualizar saldos
            if tanque_origen.Saldo is None:
                tanque_origen.Saldo = Decimal('0')
            if tanque_destino.Saldo is None:
                tanque_destino.Saldo = Decimal('0')

            tanque_origen.Saldo -= cantidad
            tanque_destino.Saldo += cantidad

            # Guardar en la base de datos
            db.session.add(nueva_transaccion)
            db.session.add(transferencia_salida)
            db.session.add(transferencia_entrada)
            db.session.commit()

            flash(f'Transferencia registrada exitosamente. Transacción ID: {transaccion_id}', 'success')
            return redirect(url_for('main.index'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error al procesar la transferencia: {str(e)}', 'error')
            return redirect(url_for('main.registro_combustible'))

    # Obtener tanques de almacenamiento (origen)
    tanques_origen = []
    tanques_destino = []
    
    # Cargar desde CSV si no hay datos en BD
    all_tanques = Tanques.query.all()
    if not all_tanques:
        tanques_csv = Tanques.cargar_desde_csv()
        for tanque in tanques_csv:
            if tanque.tipo == 'Almacenamiento':
                tanques_origen.append(tanque)
            elif tanque.tipo == 'Consumo':
                tanques_destino.append(tanque)
    else:
        for tanque in all_tanques:
            if tanque.tipo == 'Almacenamiento':
                tanques_origen.append(tanque)
            elif tanque.tipo == 'Consumo':
                tanques_destino.append(tanque)
    
    # Obtener responsables
    responsables = Responsables.query.all()
    if not responsables:
        responsables = Responsables.cargar_desde_csv()

    return render_template('registro_combustible.html', 
                         tanques_origen=tanques_origen,
                         tanques_destino=tanques_destino,
                         responsables=responsables)

@main.route('/api/tanques/<tipo>')
def api_tanques(tipo):
    """API endpoint para obtener tanques por tipo"""
    tanques = []
    all_tanques = Tanques.query.all()
    
    if not all_tanques:
        tanques_csv = Tanques.cargar_desde_csv()
        for tanque in tanques_csv:
            if tanque.tipo == tipo:
                tanques.append({
                    'TanqueId': tanque.TanqueId,
                    'Codigo': tanque.Codigo,
                    'Tipo': tanque.tipo
                })
    else:
        for tanque in all_tanques:
            if tanque.tipo == tipo:
                tanques.append({
                    'TanqueId': tanque.TanqueId,
                    'Codigo': tanque.Codigo,
                    'Tipo': tanque.tipo
                })
    
    return jsonify(tanques)

@main.route('/api/responsables')
def api_responsables():
    """API endpoint para obtener responsables con filtrado opcional"""
    query = request.args.get('q', '').lower()
    responsables = []
    
    all_responsables = Responsables.query.all()
    if not all_responsables:
        all_responsables = Responsables.cargar_desde_csv()
    
    for responsable in all_responsables:
        # Filtrar por nombre o CI si se proporciona query
        if not query or query in responsable.Nombre.lower() or query in responsable.CI:
            responsables.append({
                'ResponsableId': responsable.ResponsableId,
                'Nombre': responsable.Nombre,
                'CI': responsable.CI
            })
    
    return jsonify(responsables)