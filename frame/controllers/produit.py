
from flask import  render_template, request, redirect, url_for, Blueprint,flash
from flask_login import login_required, current_user

from frame import db

from ..models.produit import produits


produit = Blueprint('produit', __name__)




@produit.route('/produit/list')
@login_required
def list_produit():
    produitss = produits.query.all()
    return render_template("produit.html", produits = produitss, user=current_user)


@produit.route('/view_addproduit', methods = ['GET'])
@login_required
def view_addproduit():
    return render_template("addproduit.html", user=current_user)
    

@produit.route('/save_addproduit', methods = ['POST'])
@login_required
def save_addproduit():
    #default input
    etat = '1'
    retenu= '0'
    #Recuperation inputs from formulaire
    inputs = request.form
    titre = inputs['titre']
    description = inputs['desc']
    prix= inputs['prix']
    color= inputs['color']
    #Insert
    instance = produits (titre, description, prix,color)
    db.session.add(instance)
    db.session.commit()
    #flash
    flash("produit Inserted Successfully")
    #Redirect
    return redirect(url_for('produit.list_produit'))
    


@produit.route('/view_editproduit',methods = ['GET'])
@login_required
def view_editproduit():

    produit = produits.query.get(request.args.get('id'))
    return render_template("editproduit.html", produit = produit, user=current_user) 
    


@produit.route('/save_editproduit', methods = ['POST'])
@login_required
def save_editproduit():
    inputs = request.form

    fupdate = produits.query.get(inputs['id'])
    
    
    fupdate.titre           = inputs['titre']
    fupdate.description     = inputs['desc']
    fupdate.prix         = inputs['prix']
    fupdate.color   = inputs['color']

    db.session.commit()
    flash("produit Updated Successfully")

    return redirect(url_for('produit.list_produit'))
 
@produit.route('/produit/delete/<int:id>')
@login_required
def delete_produit(id):
    shit = produits.query.get(id)
    db.session.delete(shit)
    db.session.commit()
    flash("produit Deleted Successfully")
    return redirect(url_for('produit.list_produit'))
    

  

    