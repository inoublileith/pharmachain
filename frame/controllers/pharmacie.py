from flask import  render_template, request, redirect, url_for, Blueprint,flash
from flask_login import login_required, current_user

from frame import db

from ..models.pharmacie import pharmacies


pharmacie = Blueprint('pharmacie', __name__)




@pharmacie.route('/pharmacie/list')
@login_required
def list_pharmacie():
    pharmaciess = pharmacies.query.all()
    return render_template("pharmacie.html", pharmacies = pharmaciess, user=current_user)





@pharmacie.route('/view_addpharmacie', methods = ['GET'])
@login_required
def view_addpharmacie():
    return render_template("addpharmacie.html", user=current_user)
    

@pharmacie.route('/save_addpharmacie', methods = ['POST'])
@login_required
def save_addpharmacie():
    #default input
    etat = '1'
    retenu= '0'
    #Recuperation inputs from formulaire
    inputs = request.form
    nom = inputs['nom']
    gouvernorat = inputs['gouvernorat']
    ville= inputs['ville']
    
    #Insert
    instance = pharmacies(nom, gouvernorat, ville)
    db.session.add(instance)
    db.session.commit()
    #flash
    flash("pharmacie Inserted Successfully")
    #Redirect
    return redirect(url_for('pharmacie.list_pharmacie'))
    


@pharmacie.route('/view_editpharmacie',methods = ['GET'])
@login_required
def view_editpharmacie():

    pharmacie = pharmacies.query.get(request.args.get('id'))
    return render_template("editpharmacie.html", pharmacie = pharmacie, user=current_user) 
    


@pharmacie.route('/save_editpharmacie', methods = ['POST'])
@login_required
def save_editpharmacie():
    inputs = request.form

    fupdate = pharmacies.query.get(inputs['id'])
    
    
    fupdate.nom  = inputs['nom']
    fupdate.gouvernorat  = inputs['gouvernorat']
    fupdate.ville  = inputs['ville']
    

    db.session.commit()
    flash("pharmacie Updated Successfully")

    return redirect(url_for('pharmacie.list_pharmacie'))
 
@pharmacie.route('/pharmacie/delete/<int:id>')
@login_required
def delete_pharmacie(id):
    shit = pharmacies.query.get(id)
    db.session.delete(shit)
    db.session.commit()
    flash("pharmacie Deleted Successfully")
    return redirect(url_for('pharmacie.list_pharmacie'))
    