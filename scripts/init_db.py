"""
Script para inicializar datos de prueba en la aplicación
"""
import os
import sys
import csv
from datetime import datetime

# Agregar el directorio raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.tanques import Tanques
from app.models.responsables import Responsables
from config import config

def load_tanques_from_csv():
    """Cargar tanques desde el archivo CSV"""
    app = create_app()
    app.config.from_object(config['development'])
    
    with app.app_context():
        # Verificar si ya hay tanques
        if Tanques.query.first():
            print("Los tanques ya están cargados")
            return
        
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'data', 'tanques.csv')
        
        if not os.path.exists(csv_path):
            print(f"Archivo CSV no encontrado: {csv_path}")
            return
        
        tanques_creados = 0
        try:
            with open(csv_path, 'r', encoding='utf-8-sig') as file:  # utf-8-sig maneja BOM automáticamente
                reader = csv.DictReader(file, delimiter=';')
                print(f"Columnas encontradas en CSV: {reader.fieldnames}")
                for i, row in enumerate(reader, 1):
                    if i <= 3:  # Solo mostrar las primeras 3 filas para debug
                        print(f"Procesando fila {i}: {row}")
                    # Asignar saldo inicial basado en el tipo del CSV
                    saldo_inicial = 5000.0 if row['tipo'] == 'Almacenamiento' else 0.0
                    capacidad = 10000.0 if row['tipo'] == 'Almacenamiento' else 1000.0
                    
                    tanque = Tanques(
                        TanqueId=f"TQ{i:04d}",
                        Codigo=row['codigo'],
                        TipoId=row['tipo'],  # Usar directamente el tipo del CSV
                        Capacidad=capacidad,
                        Saldo=saldo_inicial,
                        Estado='ACTIVO',
                        UsuarioId='SISTEMA'
                    )
                    db.session.add(tanque)
                    tanques_creados += 1
                    
                    # Commit cada 50 registros para evitar problemas
                    if i % 50 == 0:
                        db.session.commit()
                        print(f"Procesados {i} tanques...")
        
            db.session.commit()
            print(f"Se cargaron {tanques_creados} tanques exitosamente")
        except Exception as e:
            print(f"Error al cargar tanques: {e}")
            db.session.rollback()

def load_responsables_from_csv():
    """Cargar responsables desde el archivo CSV"""
    app = create_app()
    app.config.from_object(config['development'])
    
    with app.app_context():
        # Verificar si ya hay responsables
        if Responsables.query.first():
            print("Los responsables ya están cargados")
            return
        
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'data', 'personal.csv')
        
        if not os.path.exists(csv_path):
            print(f"Archivo CSV no encontrado: {csv_path}")
            return
        
        responsables_creados = 0
        try:
            with open(csv_path, 'r', encoding='utf-8-sig') as file:  # utf-8-sig maneja BOM
                reader = csv.DictReader(file, delimiter=';')
                print(f"Columnas encontradas en CSV responsables: {reader.fieldnames}")
                for i, row in enumerate(reader, 1):
                    if i <= 3:  # Debug para las primeras 3 filas
                        print(f"Procesando responsable {i}: {row}")
                    responsable = Responsables(
                        ResponsableId=row['CI'],
                        Nombre=row['Nombre'],
                        CI=row['CI'],
                        Estado='ACTIVO'
                    )
                    db.session.add(responsable)
                    responsables_creados += 1
                    
                    # Commit cada 50 registros
                    if i % 50 == 0:
                        db.session.commit()
                        print(f"Procesados {i} responsables...")
        
            db.session.commit()
            print(f"Se cargaron {responsables_creados} responsables exitosamente")
        except Exception as e:
            print(f"Error al cargar responsables: {e}")
            db.session.rollback()

def init_database():
    """Inicializar la base de datos con datos de prueba"""
    app = create_app()
    app.config.from_object(config['development'])
    
    with app.app_context():
        # Crear tablas
        db.create_all()
        print("Tablas creadas")
        
        # Cargar datos
        load_tanques_from_csv()
        load_responsables_from_csv()
        
        print("Inicialización completada!")

if __name__ == '__main__':
    init_database()
