from datetime import datetime
from sqlalchemy import Column, String, Numeric, DateTime, Integer
from app import db
import csv
import os

class Tanques(db.Model):
    __tablename__ = 'tanques'

    Fila = Column(Integer, nullable=True)
    TanqueId = Column(String, primary_key=True)
    Codigo = Column(String, nullable=False)
    TipoId = Column(String, nullable=False)
    Capacidad = Column(Numeric(10,2), nullable=False, default=0)
    Saldo = Column(Numeric(10,2), nullable=True, default=0)
    MaquinariaId = Column(String, nullable=True)
    Combustible = Column(String, nullable=True)
    Estado = Column(String, nullable=False, default='A')
    FechaRegistro = Column(DateTime, default=datetime.utcnow)
    UsuarioId = Column(String, nullable=False, default='SISTEMA')
    Tolerancia = Column(Integer, nullable=False, default=0)

    # Propiedad calculada para obtener el tipo basado en TipoId del CSV
    @property
    def tipo(self):
        # Usar directamente el TipoId del CSV que es más confiable
        return self.TipoId

    def __repr__(self):
        return f'<Tanque {self.Codigo} - {self.tipo}>'

    @classmethod
    def cargar_desde_csv(cls):
        """Método para cargar tanques desde el archivo CSV"""
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'tanques.csv')
        
        tanques = []
        with open(csv_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')
            for i, row in enumerate(reader, 1):
                # Asignar saldo inicial basado en el tipo
                saldo_inicial = 5000.0 if row['tipo'] == 'Almacenamiento' else 0.0
                
                tanque = cls(
                    TanqueId=f"TQ{i:04d}",
                    Codigo=row['codigo'],
                    TipoId=row['tipo'],  # Usar directamente el tipo del CSV
                    Capacidad=10000.0 if row['tipo'] == 'Almacenamiento' else 1000.0,  # Más capacidad para almacenamiento
                    Saldo=saldo_inicial
                )
                tanques.append(tanque)
        
        return tanques