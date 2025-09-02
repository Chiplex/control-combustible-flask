#!/usr/bin/env python3
"""
WSGI file para PythonAnywhere - Control de Combustible
Configuración optimizada para SQLite y despliegue rápido
"""

import sys
import os

# Agregar el directorio del proyecto al path de Python
# CAMBIAR 'yourusername' por tu usuario real de PythonAnywhere
project_home = '/home/yourusername/control-combustible-flask'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Configurar el entorno para producción
os.environ['FLASK_CONFIG'] = 'production'

# Importar la aplicación
from app import create_app, db

# Crear la aplicación con configuración de producción
app = create_app()

# Función para inicializar la base de datos
def initialize_database():
    """Inicializar la base de datos SQLite si es necesario"""
    with app.app_context():
        try:
            # Crear todas las tablas si no existen
            db.create_all()
            
            # Cargar datos iniciales desde CSV solo si las tablas están vacías
            from app.models.tanques import Tanques
            from app.models.responsables import Responsables
            
            # Verificar y cargar tanques
            if Tanques.query.first() is None:
                tanques_csv = Tanques.cargar_desde_csv()
                for tanque in tanques_csv:
                    db.session.add(tanque)
                db.session.commit()
                
            # Verificar y cargar responsables
            if Responsables.query.first() is None:
                responsables_csv = Responsables.cargar_desde_csv()
                for responsable in responsables_csv:
                    db.session.add(responsable)
                db.session.commit()
                
        except Exception as e:
            # Los errores aparecerán en los logs de PythonAnywhere
            print(f"Error inicializando base de datos: {e}")

# Inicializar la base de datos una vez al cargar
initialize_database()

# Esta es la aplicación WSGI que PythonAnywhere utilizará
application = app

if __name__ == "__main__":
    application.run(debug=False)
