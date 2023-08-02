from frame import db
from sqlalchemy.sql import func

class grossistes (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150))
    prenom = db.Column(db.String(150))
    tel = db.Column(db.Integer)
   
    
    def __init__(self, nom, prenom,tel):
 
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
      



