from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    app = Flask(__name__)
    
    # Configuración por defecto para SQLite
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
    
    from config import config
    app.config.from_object(config[config_name])
    
    # Asegurar que hay una URI de base de datos configurada
    if not app.config.get('SQLALCHEMY_DATABASE_URI'):
        # Configuración de emergencia para SQLite
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "..", "control_combustible.db")}'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .routes import transferencias as transferencias_blueprint
    app.register_blueprint(transferencias_blueprint)

    return app