from collections import UserDict
from optparse import IndentedHelpFormatter
from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class vente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    pharmacie_id = db.Column(db.Integer, db.ForeignKey('pharmacie.id'))
    produit_id = db.Column(db.Integer, db.ForeignKey('produit.id'))


class pharmacie(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150), unique=True)
    gouvernorat = db.Column(db.String(150))
    ville = db.Column(db.String(150))
    ventes = db.relationship('vente')

class produit(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150), unique=True)
    desc = db.Column(db.String(150))
    prix = db.Column(db.int(150))
    color = db.Column(db.String(150))
    ventes = db.relationship('vente')
    ventes = db.relationship('livraison')


class livraison(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adresse_livraison= db.Column(db.String(10000))
    date_depart= db.column(db.DateTime(timezone=True), default=func.now())
    date_arrive= db.column(db.DateTime(timezone=True), default=func.now())
    grossiste_id = db.Column(db.Integer, db.ForeignKey('grossiste.id'))
    produit_id = db.Column(db.Integer, db.ForeignKey('produit.id'))

    class grossiste(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150), unique=True)
    prenom = db.Column(db.String(150))
    tel = db.Column(db.int(150))
    livraisons = db.relationship('livraison')


    class laboratoire(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150), unique=True)
    gouvernorat = db.Column(db.String(150))
    ville = db.Column(db.int(150))
    livraisons = db.relationship('livraison')
