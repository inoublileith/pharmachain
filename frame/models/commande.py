from frame import db
from sqlalchemy.sql import func

class commandes (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150))
    reference = db.Column(db.String(150))


    def __init__(self, nom, reference):
 
        self.nom = nom
        self.reference = reference
     
     
      


