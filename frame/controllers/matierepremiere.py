from flask import  render_template, request, redirect, url_for, Blueprint,flash
from flask_login import login_required, current_user

from frame import db

from ..models.matierepremiere import matierespremieres


matierepremiere = Blueprint('matierepremiere', __name__)




@matierepremiere.route('/matierepremiere/list')
@login_required
def list_matierepremiere():
    matierespremieress = matierespremieres.query.all()
    return render_template("matierepremiere.html", matierespremieres = matierespremieress, user=current_user)





@matierepremiere.route('/view_addmatierepremiere', methods = ['GET'])
@login_required
def view_addmatierepremiere():
    return render_template("addmatierepremiere.html", user=current_user)
    

@matierepremiere.route('/save_addmatierepremiere', methods = ['POST'])
@login_required
def save_addmatierepremiere():
    #default input
    etat = '1'
    retenu= '0'
    #Recuperation inputs from formulaire
    inputs = request.form
    nom = inputs['nom']
    type = inputs['type']
    composition= inputs['composition']
   
    
    #Insert
    instance = matierespremieres(nom, type, composition)
    db.session.add(instance)
    db.session.commit()
    #flash
    flash("matierepremiere Inserted Successfully")
    #Redirect
    return redirect(url_for('matierepremiere.list_matierepremiere'))
    


@matierepremiere.route('/view_editmatierepremiere',methods = ['GET'])
@login_required
def view_editmatierepremiere():

    matierepremiere = matierespremieres.query.get(request.args.get('id'))
    return render_template("editmatierepremiere.html", matierepremiere = matierepremiere, user=current_user) 
    


@matierepremiere.route('/save_editmatierepremiere', methods = ['POST'])
@login_required
def save_editmatierepremiere():
    inputs = request.form

    fupdate = matierespremieres.query.get(inputs['id'])
    
    
    fupdate.nom  = inputs['nom']
    fupdate.type  = inputs['type']
    fupdate.composition  = inputs['composition']
    
    

    db.session.commit()
    flash("matierepremiere Updated Successfully")

    return redirect(url_for('matierepremiere.list_matierepremiere'))
 
@matierepremiere.route('/matierepremiere/delete/<int:id>')
@login_required
def delete_matierepremiere(id):
    shit = matierespremieres.query.get(id)
    db.session.delete(shit)
    db.session.commit()
    flash("matierepremiere Deleted Successfully")
    return redirect(url_for('matierepremiere.list_matierepremiere'))
    