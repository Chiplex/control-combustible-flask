from app import db

class Responsables(db.Model):
    __tablename__ = 'responsables'

    ResponsableId = db.Column(db.String(50), primary_key=True)
    Nombre = db.Column(db.String(255), nullable=False)
    CI = db.Column(db.String(20), nullable=False)
    Estado = db.Column(db.String(20), default='ACTIVO')

    def __repr__(self):
        return f'<Responsable {self.Nombre}>'

    @classmethod
    def cargar_desde_csv(cls):
        """Método para cargar responsables desde el archivo CSV"""
        import csv
        import os
        
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'personal.csv')
        
        responsables = []
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                responsable = cls(
                    ResponsableId=row['CI'],
                    Nombre=row['Nombre'],
                    CI=row['CI']
                )
                responsables.append(responsable)
        
        return responsables
