from frame import db
from sqlalchemy.sql import func

class analystes (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150))
    prenom = db.Column(db.String(150))
   
    
    def __init__(self, nom, prenom):
 
        self.nom = nom
        self.prenom = prenom
        
      



