from flask import  render_template, request, redirect, url_for, Blueprint,flash
from flask_login import login_required, current_user

from frame import db

from ..models.grossiste import grossistes


grossiste = Blueprint('grossiste', __name__)




@grossiste.route('/grossiste/list')
@login_required
def list_grossiste():
    grossistess = grossistes.query.all()
    return render_template("grossiste.html", grossistes = grossistess, user=current_user)





@grossiste.route('/view_addgrossiste', methods = ['GET'])
@login_required
def view_addgrossiste():
    return render_template("addgrossiste.html", user=current_user)
    

@grossiste.route('/save_addgrossiste', methods = ['POST'])
@login_required
def save_addgrossiste():
    #default input
    etat = '1'
    retenu= '0'
    #Recuperation inputs from formulaire
    inputs = request.form
    nom = inputs['nom']
    prenom = inputs['prenom']
    tel= inputs['tel']
    
    #Insert
    instance = grossistes(nom, prenom,tel)
    db.session.add(instance)
    db.session.commit()
    #flash
    flash("grossiste Inserted Successfully")
    #Redirect
    return redirect(url_for('grossiste.list_grossiste'))
    


@grossiste.route('/view_editgrossiste',methods = ['GET'])
@login_required
def view_editgrossiste():

    grossiste = grossistes.query.get(request.args.get('id'))
    return render_template("editgrossiste.html", grossiste = grossiste, user=current_user) 
    


@grossiste.route('/save_editgrossiste', methods = ['POST'])
@login_required
def save_editgrossiste():
    inputs = request.form

    fupdate = grossistes.query.get(inputs['id'])
    
    
    fupdate.nom  = inputs['nom']
    fupdate.prenom  = inputs['prenom']
    fupdate.tel  = inputs['tel']
    

    db.session.commit()
    flash("grossiste Updated Successfully")

    return redirect(url_for('grossiste.list_grossiste'))
 
@grossiste.route('/grossiste/delete/<int:id>')
@login_required
def delete_grossiste(id):
    shit = grossistes.query.get(id)
    db.session.delete(shit)
    db.session.commit()
    flash("grossiste Deleted Successfully")
    return redirect(url_for('grossiste.list_grossiste'))
    