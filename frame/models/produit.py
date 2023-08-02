from frame import db
from sqlalchemy.sql import func

class produits (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150))
    description = db.Column(db.String(1000))
    prix = db.Column(db.Integer)
    color = db.Column(db.String(5000))
   
    
    def __init__(self, titre, description, prix, color):
 
        self.titre = titre
        self.description = description
        self.prix = prix
        self.color = color
      
        