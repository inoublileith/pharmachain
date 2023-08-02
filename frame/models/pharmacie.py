
from frame import db
from sqlalchemy.sql import func

class pharmacies (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150))
    gouvernorat = db.Column(db.String(1000))
    ville = db.Column(db.String(1000))
   
    
    def __init__(self, nom, gouvernorat, ville):
 
        self.nom = nom
        self.gouvernorat = gouvernorat
        self.ville = ville
      