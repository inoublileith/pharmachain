from frame import db
from sqlalchemy.sql import func

class matierespremieres (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150))
    type = db.Column(db.String(150))
    composition = db.Column(db.String(1000))

   
    
    def __init__(self, nom, type, composition):
 
        self.nom = nom
        self.type = type
        self.composition = composition
      





