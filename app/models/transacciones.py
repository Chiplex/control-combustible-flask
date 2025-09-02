from datetime import datetime
from sqlalchemy import Column, String, DateTime
from app import db

class Transacciones(db.Model):
    __tablename__ = 'transacciones'

    Fila = Column(db.Integer, primary_key=True, autoincrement=True)
    TransaccionId = Column(String, nullable=False)
    Detalles = Column(String, nullable=True)
    FechaRegistro = Column(DateTime, default=datetime.utcnow)
    UsuarioId = Column(String, nullable=True)
    Estado = Column(String, nullable=True)

    def __repr__(self):
        return f'<Transaccion {self.TransaccionId}>'