from frame import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# !type w clé primaire wl longueur wl relationship hhhhhh
# kif nbadlou fel model ylzmna nbadlou fl base de donnée
# UserMixin -> besh tgoul ll app elli hedha l class main
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150))
    prenom = db.Column(db.String(150))
    tel = db.Column(db.Integer)
    email = db.Column(db.String(150))
    adresse = db.Column(db.String(150))
    cpostal = db.Column(db.Integer)
    gouvernorat = db.Column(db.String(150))
    login = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))
    profil = db.Column(db.Integer)
    permissions = db.Column(db.Integer)
    avatar = db.Column(db.String(150))
    date_ins = db.Column(db.DateTime(timezone=True), default=func.now())
    date_upd = db.Column(db.DateTime(timezone=True), default=func.now())
    etat = db.Column(db.Integer)
    
    def __init__(self, nom, prenom, tel, email, adresse, cpostal,gouvernorat,login,password,profil,permissions, avatar,date_ins,date_upd, etat  ):
    
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.email = email
        self.adresse = adresse
        self.cpostal = cpostal
        self.gouvernorat = gouvernorat
        self.login = login
        self.password = password
        self.profil = profil
        self.permissions = permissions
        self.avatar = avatar
        self.date_ins = date_ins
        self.date_upd = date_upd
        self.etat = etat
        

