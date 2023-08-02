from flask import  render_template, request, redirect, url_for, Blueprint,flash
from flask_login import login_required, current_user

from frame import db

from ..models.commande import commandes


commande = Blueprint('commande', __name__)




@commande.route('/commande/list')
@login_required
def list_commande():
    commandess = commandes.query.all()
    return render_template("commande.html", commandes = commandess, user=current_user)





@commande.route('/view_addcommande', methods = ['GET'])
@login_required
def view_addcommande():
    return render_template("addcommande.html", user=current_user)
    

@commande.route('/save_addcommande', methods = ['POST'])
@login_required
def save_addcommande():
    #default input
    etat = '1'
    retenu= '0'
    #Recuperation inputs from formulaire
    inputs = request.form
    nom = inputs['nom']
    reference = inputs['reference']
    
    
    #Insert
    instance = commandes(nom, reference)
    db.session.add(instance)
    db.session.commit()
    #flash
    flash("commande Inserted Successfully")
    #Redirect
    return redirect(url_for('commande.list_commande'))
    


@commande.route('/view_editcommande',methods = ['GET'])
@login_required
def view_editcommande():

    commande = commandes.query.get(request.args.get('id'))
    return render_template("editcommande.html", commande = commande, user=current_user) 
    


@commande.route('/save_editcommande', methods = ['POST'])
@login_required
def save_editcommande():
    inputs = request.form

    fupdate = commandes.query.get(inputs['id'])
    
    
    fupdate.nom  = inputs['nom']
    fupdate.reference  = inputs['reference']
   
    

    db.session.commit()
    flash("commande Updated Successfully")

    return redirect(url_for('commande.list_commande'))
 
@commande.route('/commande/delete/<int:id>')
@login_required
def delete_commande(id):
    shit = commandes.query.get(id)
    db.session.delete(shit)
    db.session.commit()
    flash("commande Deleted Successfully")
    return redirect(url_for('commande.list_commande'))
    