from frame import db
from sqlalchemy.sql import func

class recommandations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150))
    description = db.Column(db.String(1000))
    domaine = db.Column(db.String(1000))
    specification = db.Column(db.String(5000))
    retenu = db.Column(db.Integer)
    etat = db.Column(db.Integer)
    date_ins = db.Column(db.DateTime(timezone=True), default=func.now())
    
    def __init__(self, titre, description, domaine, specification, retenu, etat):
 
        self.titre = titre
        self.description = description
        self.domaine = domaine
        self.specification = specification
        self.retenu = retenu
        self.etat = etat
        
        