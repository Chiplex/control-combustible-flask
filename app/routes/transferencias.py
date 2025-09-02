from flask import Blueprint, request, jsonify
from app.models.transferencias import Transferencias
from app import db

from flask import Blueprint, render_template, request, jsonify
from app.models.transferencias import Transferencias
from app.models.tanques import Tanques
from app.models.responsables import Responsables
from app import db
from sqlalchemy import desc

transferencias = Blueprint('transferencias', __name__, url_prefix='/transferencias')

@transferencias.route('/')
def listar():
    """Listar todas las transferencias"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    # Filtros
    tipo_filtro = request.args.get('tipo', '')
    fecha_desde = request.args.get('fecha_desde', '')
    fecha_hasta = request.args.get('fecha_hasta', '')
    
    query = Transferencias.query.order_by(desc(Transferencias.FechaRegistro))
    
    if tipo_filtro:
        query = query.filter(Transferencias.Tipo == tipo_filtro)
    
    if fecha_desde:
        from datetime import datetime
        fecha_desde_dt = datetime.strptime(fecha_desde, '%Y-%m-%d')
        query = query.filter(Transferencias.FechaTransferencia >= fecha_desde_dt)
    
    if fecha_hasta:
        from datetime import datetime
        fecha_hasta_dt = datetime.strptime(fecha_hasta, '%Y-%m-%d')
        query = query.filter(Transferencias.FechaTransferencia <= fecha_hasta_dt)
    
    transferencias_pag = query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('transferencias/listar.html', 
                         transferencias=transferencias_pag.items,
                         pagination=transferencias_pag,
                         tipo_filtro=tipo_filtro,
                         fecha_desde=fecha_desde,
                         fecha_hasta=fecha_hasta)

@transferencias.route('/detalle/<transaccion_id>')
def detalle(transaccion_id):
    """Ver detalle de una transacción específica"""
    transfers = Transferencias.query.filter_by(TransaccionId=transaccion_id).all()
    
    if not transfers:
        return render_template('error.html', 
                             mensaje="Transacción no encontrada"), 404
    
    # Obtener información adicional
    tanques_info = {}
    responsables_info = {}
    
    for transfer in transfers:
        if transfer.TanqueId not in tanques_info:
            tanque = Tanques.query.filter_by(TanqueId=transfer.TanqueId).first()
            if tanque:
                tanques_info[transfer.TanqueId] = tanque
        
        if transfer.ResponsableId not in responsables_info:
            responsable = Responsables.query.filter_by(ResponsableId=transfer.ResponsableId).first()
            if responsable:
                responsables_info[transfer.ResponsableId] = responsable
    
    return render_template('transferencias/detalle.html',
                         transferencias=transfers,
                         tanques_info=tanques_info,
                         responsables_info=responsables_info,
                         transaccion_id=transaccion_id)

@transferencias.route('/api/resumen')
def api_resumen():
    """API para obtener resumen de transferencias"""
    from datetime import datetime, timedelta
    
    hoy = datetime.now()
    hace_7_dias = hoy - timedelta(days=7)
    hace_30_dias = hoy - timedelta(days=30)
    
    # Transferencias de hoy
    hoy_count = Transferencias.query.filter(
        Transferencias.FechaRegistro >= hoy.replace(hour=0, minute=0, second=0)
    ).count()
    
    # Transferencias últimos 7 días
    semana_count = Transferencias.query.filter(
        Transferencias.FechaRegistro >= hace_7_dias
    ).count()
    
    # Transferencias último mes
    mes_count = Transferencias.query.filter(
        Transferencias.FechaRegistro >= hace_30_dias
    ).count()
    
    return jsonify({
        'hoy': hoy_count,
        'semana': semana_count,
        'mes': mes_count
    })