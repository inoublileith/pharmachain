from flask import Flask

from flask_mysqldb import MySQL

from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager



#Instance app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#Connexion Mysql
# app.config['MYSQL_HOST'] = '192.168.10.10'
# app.config['MYSQL_USER'] = 'homestead'
# app.config['MYSQL_PASSWORD'] = 'secret'
# app.config['MYSQL_DB'] = 'homestead'

# mysql = MySQL(app)

#Connexion db
db = SQLAlchemy()
DB_NAME = "homestead"
# l format te3 l URI : driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@localhost/homestead"

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


#func create APP
def getRoutes ():   
    
    #Controllers + BLueprint

    from .controllers.auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from .controllers.routes import routes
    app.register_blueprint(routes, url_prefix='/')

    from .controllers.rec import recommandation
    app.register_blueprint(recommandation, url_prefix='/')
    
    from .controllers.analyste import analyste
    app.register_blueprint(analyste, url_prefix='/')

    from .controllers.fournisseur import fournisseur
    app.register_blueprint(fournisseur, url_prefix='/')

    from .controllers.laboratoire import laboratoire
    app.register_blueprint(laboratoire, url_prefix='/')

    from .controllers.commande import commande
    app.register_blueprint(commande, url_prefix='/')

    from .controllers.matierepremiere import matierepremiere
    app.register_blueprint(matierepremiere, url_prefix='/')

    from .controllers.pharmacie import pharmacie
    app.register_blueprint(pharmacie, url_prefix='/')
    
    from .controllers.grossiste import grossiste
    app.register_blueprint(grossiste, url_prefix='/')

    from .controllers.produit import produit
    app.register_blueprint(produit, url_prefix='/')

    from .controllers.patient import patient
    app.register_blueprint(patient, url_prefix='/')
    
    #Api
    from .api.api_rec import api_recommandations
    app.register_blueprint(api_recommandations, url_prefix='/')

    from .api.api_analyste import api_analystes
    app.register_blueprint(api_analystes, url_prefix='/')

    from .api.api_fournisseur import api_fournisseurs
    app.register_blueprint(api_fournisseurs, url_prefix='/')

    from .api.api_laboratoire import api_laboratoires
    app.register_blueprint(api_laboratoires, url_prefix='/')

    from .api.api_commande import api_commandes
    app.register_blueprint(api_commandes, url_prefix='/')

    from .api.api_matierepremiere import api_matierespremieres
    app.register_blueprint(api_matierespremieres, url_prefix='/')

    from .api.api_pharmacie import api_pharmacies
    app.register_blueprint(api_pharmacies, url_prefix='/')

    from .api.api_grossiste import api_grossistes
    app.register_blueprint(api_grossistes, url_prefix='/')

    from .api.api_produit import api_produits
    app.register_blueprint(api_produits, url_prefix='/')

    
    
    #Models
    # from .models <- esm dossier .user <- esm l fichier import User <- esm l class
    from .models.user import User
    from .models.recommandation import recommandations
    from .models.analyste import analystes
    from .models.fournisseur import fournisseurs
    from .models.laboratoire import laboratoires
    from .models.commande import commandes
    from .models.matierepremiere import matierespremieres
    from .models.pharmacie import pharmacies
    from .models.grossiste import grossistes
    from .models.produit import produits


    #Login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('frame/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')