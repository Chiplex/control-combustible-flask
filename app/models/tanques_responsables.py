from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
from app import db

class TanquesResponsables(db.Model):
    __tablename__ = 'tanques_responsables'

    Fila = Column(Integer, nullable=True)
    TanqueResponsableId = Column(String, primary_key=True)
    TanqueId = Column(String, nullable=False)
    ResponsableId = Column(String, nullable=False)
    FechaRegistro = Column(DateTime, default=datetime.utcnow)
    Estado = Column(String, nullable=False)
    UsuarioId = Column(String, nullable=False)

    Tanque = Column(String, nullable=True)
    Responsable = Column(String, nullable=True)