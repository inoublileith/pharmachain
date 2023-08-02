from flask import  render_template, request, redirect, url_for, Blueprint,flash
from flask_login import login_required, current_user

from frame import db

from ..models.patient import patients


patient = Blueprint('patient', __name__)




@patient.route('/patient/list')
@login_required
def list_patient():
    patientss = patients.query.all()
    return render_template("patient.html", patients = patientss, user=current_user)





@patient.route('/view_addpatient', methods = ['GET'])
@login_required
def view_addpatient():
    return render_template("addpatient.html", user=current_user)
    

@patient.route('/save_addpatient', methods = ['POST'])
@login_required
def save_addpatient():
    #default input
    etat = '1'
    retenu= '0'
    #Recuperation inputs from formulaire
    inputs = request.form
    nom = inputs['nom']
    prenom = inputs['prenom']
    email= inputs['email']
    tel= inputs['tel']
    
    #Insert
    instance = patients(nom, prenom, email,tel)
    db.session.add(instance)
    db.session.commit()
    #flash
    flash("patient Inserted Successfully")
    #Redirect
    return redirect(url_for('patient.list_patient'))
    


@patient.route('/view_editpatient',methods = ['GET'])
@login_required
def view_editpatient():

    patient = patients.query.get(request.args.get('id'))
    return render_template("editpatient.html", patient = patient, user=current_user) 
    


@patient.route('/save_editpatient', methods = ['POST'])
@login_required
def save_editpatient():
    inputs = request.form

    fupdate = patients.query.get(inputs['id'])
    
    
    fupdate.nom  = inputs['nom']
    fupdate.prenom  = inputs['prenom']
    fupdate.email  = inputs['email']
    fupdate.tel  = inputs['tel']
    

    db.session.commit()
    flash("patient Updated Successfully")

    return redirect(url_for('patient.list_patient'))
 
@patient.route('/patient/delete/<int:id>')
@login_required
def delete_patient(id):
    shit = patients.query.get(id)
    db.session.delete(shit)
    db.session.commit()
    flash("patient Deleted Successfully")
    return redirect(url_for('patient.list_patient'))
    