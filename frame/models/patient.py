from frame import db
from sqlalchemy.sql import func

class patients (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150))
    prenom = db.Column(db.String(150))
    email = db.Column(db.String(1000))
    tel = db.Column(db.Integer)
   
    
    def __init__(self, nom, prenom, email,tel):
 
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.tel = tel
      


