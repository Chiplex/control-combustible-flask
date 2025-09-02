import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'control-combustible-secret-key-2025'
    
    # SQLite para desarrollo y PythonAnywhere
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'control_combustible.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # Cambiar a True para debug
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    # Para PythonAnywhere también usaremos SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join('/home/yourusername/', 'control_combustible.db')
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}