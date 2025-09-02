from datetime import datetime
from sqlalchemy import Column, String, Numeric, DateTime, Integer
from app import db
import uuid

class Transferencias(db.Model):
    __tablename__ = 'transferencias'

    Fila = Column(Integer, primary_key=True, autoincrement=True)
    TransferenciaId = Column(String, nullable=False, default=lambda: str(uuid.uuid4()))
    TanqueId = Column(String, nullable=False)
    ResponsableId = Column(String, nullable=False)
    RecepcionId = Column(String, nullable=True)
    Cantidad = Column(Numeric(10,2), nullable=False)
    Tipo = Column(String, nullable=True)  # 'SALIDA' o 'ENTRADA'
    Detalles = Column(String, nullable=True)
    ParteDiarioId = Column(String, nullable=True)
    Horometro = Column(Numeric(10,2), nullable=True)
    Odometro = Column(Numeric(10,2), nullable=True)
    FechaTransferencia = Column(DateTime, default=datetime.utcnow)
    TransaccionId = Column(String, nullable=True)
    Estado = Column(String, nullable=True, default='ACTIVO')
    FechaRegistro = Column(DateTime, default=datetime.utcnow)
    UsuarioId = Column(String, nullable=False)

    def __repr__(self):
        return f'<Transferencia {self.TransferenciaId} - {self.Tipo}>'