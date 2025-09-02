import os
from app import create_app, db
from config import config

# Obtener la configuración del entorno
config_name = os.environ.get('FLASK_CONFIG', 'development')
app = create_app()
app.config.from_object(config[config_name])

def initialize_database():
    """Inicializar la base de datos y cargar datos desde CSV"""
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        print("✅ Tablas creadas exitosamente")
        
        # Cargar datos iniciales desde CSV
        from app.models.tanques import Tanques
        from app.models.responsables import Responsables
        
        # Verificar si ya hay datos
        if Tanques.query.first() is None:
            print("📊 Cargando tanques desde CSV...")
            tanques_csv = Tanques.cargar_desde_csv()
            for tanque in tanques_csv:
                db.session.add(tanque)
            db.session.commit()
            print(f"✅ {len(tanques_csv)} tanques cargados")
        
        if Responsables.query.first() is None:
            print("👥 Cargando responsables desde CSV...")
            responsables_csv = Responsables.cargar_desde_csv()
            for responsable in responsables_csv:
                db.session.add(responsable)
            db.session.commit()
            print(f"✅ {len(responsables_csv)} responsables cargados")
            
        print("🎉 Base de datos inicializada correctamente")

if __name__ == "__main__":
    # Inicializar base de datos
    initialize_database()
    
    # Ejecutar la aplicación
    print(f"🚀 Iniciando aplicación en modo {config_name}")
    print("📱 Accede a: http://localhost:5000")
    app.run(debug=(config_name == 'development'), host='0.0.0.0', port=5000)