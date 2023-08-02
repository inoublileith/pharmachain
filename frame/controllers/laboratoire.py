from flask import  render_template, request, redirect, url_for, Blueprint,flash
from flask_login import login_required, current_user

from frame import db

from ..models.laboratoire import laboratoires


laboratoire = Blueprint('laboratoire', __name__)




@laboratoire.route('/laboratoire/list')
@login_required
def list_laboratoire():
    laboratoiress = laboratoires.query.all()
    return render_template("laboratoire.html", laboratoires = laboratoiress, user=current_user)





@laboratoire.route('/view_addlaboratoire', methods = ['GET'])
@login_required
def view_addlaboratoire():
    return render_template("addlaboratoire.html", user=current_user)
    

@laboratoire.route('/save_addlaboratoire', methods = ['POST'])
@login_required
def save_addlaboratoire():
    #default input
    etat = '1'
    retenu= '0'
    #Recuperation inputs from formulaire
    inputs = request.form
    nom = inputs['nom']
    gouvernorat = inputs['gouvernorat']
    ville= inputs['ville']
    
    #Insert
    instance = laboratoires(nom, gouvernorat, ville)
    db.session.add(instance)
    db.session.commit()
    #flash
    flash("laboratoire Inserted Successfully")
    #Redirect
    return redirect(url_for('laboratoire.list_laboratoire'))
    


@laboratoire.route('/view_editlaboratoire',methods = ['GET'])
@login_required
def view_editlaboratoire():

    laboratoire = laboratoires.query.get(request.args.get('id'))
    return render_template("editlaboratoire.html", laboratoire = laboratoire, user=current_user) 
    


@laboratoire.route('/save_editlaboratoire', methods = ['POST'])
@login_required
def save_editlaboratoire():
    inputs = request.form

    fupdate = laboratoires.query.get(inputs['id'])
    
    
    fupdate.nom  = inputs['nom']
    fupdate.gouvernorat  = inputs['gouvernorat']
    fupdate.ville  = inputs['ville']
    

    db.session.commit()
    flash("laboratoire Updated Successfully")

    return redirect(url_for('laboratoire.list_laboratoire'))
 
@laboratoire.route('/laboratoire/delete/<int:id>')
@login_required
def delete_laboratoire(id):
    shit = laboratoires.query.get(id)
    db.session.delete(shit)
    db.session.commit()
    flash("laboratoire Deleted Successfully")
    return redirect(url_for('laboratoire.list_laboratoire'))
    