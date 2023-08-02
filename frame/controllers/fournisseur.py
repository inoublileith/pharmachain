from flask import  render_template, request, redirect, url_for, Blueprint,flash
from flask_login import login_required, current_user

from frame import db

from ..models.fournisseur import fournisseurs


fournisseur = Blueprint('fournisseur', __name__)




@fournisseur.route('/fournisseur/list')
@login_required
def list_fournisseur():
    fournisseurss = fournisseurs.query.all()
    return render_template("fournisseur.html", fournisseurs = fournisseurss, user=current_user)





@fournisseur.route('/view_addfournisseur', methods = ['GET'])
@login_required
def view_addfournisseur():
    return render_template("addfournisseur.html", user=current_user)
    

@fournisseur.route('/save_addfournisseur', methods = ['POST'])
@login_required
def save_addfournisseur():
    #default input
    etat = '1'
    retenu= '0'
    #Recuperation inputs from formulaire
    inputs = request.form
    nom = inputs['nom']
    prenom = inputs['prenom']
    tel= inputs['tel']
    
    #Insert
    instance = fournisseurs(nom, prenom,tel)
    db.session.add(instance)
    db.session.commit()
    #flash
    flash("fournisseur Inserted Successfully")
    #Redirect
    return redirect(url_for('fournisseur.list_fournisseur'))
    


@fournisseur.route('/view_editfournisseur',methods = ['GET'])
@login_required
def view_editfournisseur():

    fournisseur = fournisseurs.query.get(request.args.get('id'))
    return render_template("editfournisseur.html", fournisseur = fournisseur, user=current_user) 
    


@fournisseur.route('/save_editfournisseur', methods = ['POST'])
@login_required
def save_editfournisseur():
    inputs = request.form

    fupdate = fournisseurs.query.get(inputs['id'])
    
    
    fupdate.nom  = inputs['nom']
    fupdate.prenom  = inputs['prenom']
    fupdate.tel  = inputs['tel']
    

    db.session.commit()
    flash("fournisseur Updated Successfully")

    return redirect(url_for('fournisseur.list_fournisseur'))
 
@fournisseur.route('/fournisseur/delete/<int:id>')
@login_required
def delete_fournisseur(id):
    shit = fournisseurs.query.get(id)
    db.session.delete(shit)
    db.session.commit()
    flash("fournisseur Deleted Successfully")
    return redirect(url_for('fournisseur.list_fournisseur'))
    