
from flask import  render_template, request, redirect, url_for, Blueprint,flash
from flask_login import login_required, current_user

from frame import db

from ..models.recommandation import recommandations


recommandation = Blueprint('recommandation', __name__)




@recommandation.route('/recommandation/list')
@login_required
def list_recommandation():
    # esm l variable mouch nafs esm l class !!!!!!
    # nbadlou l essm fy s thenya besh naaml difference bin les variables 
    recommandation = recommandations.query.all()
    return render_template("recommandation.html", recommandations = recommandation, user=current_user)
    # return render_template <- traja3 template ("recommandation.html", <- esm l template recommandations <- l variable ly besh yemchy ll template = recommandation, <- l variable ly fih l donnees ml base de donees/ user=current_user <- l utilisateur ly 7all twa fl session)





@recommandation.route('/view_addrec', methods = ['GET'])
@login_required
def view_addrec():
    return render_template("addrec.html", user=current_user)
    

@recommandation.route('/save_addrec', methods = ['POST'])
@login_required
def save_addrec():
    #default input
    etat = '1'
    retenu= '0'
    #Recuperation inputs from formulaire
    inputs = request.form
    titre = inputs['titre']
    description = inputs['description']
    domaine= inputs['domaine']
    specification= inputs['specification']
    #Insert
    instance = recommandations(titre, description, domaine, specification, retenu, etat)
    db.session.add(instance)
    db.session.commit()
    #flash
    flash("Recommandation Inserted Successfully")
    #Redirect
    return redirect(url_for('recommandation.list_recommandation'))
    


@recommandation.route('/view_editrec',methods = ['GET'])
@login_required
def view_editrec():

    recommandation = recommandations.query.get(request.args.get('id'))
    return render_template("editrec.html", recommandation = recommandation, user=current_user) 
    


@recommandation.route('/save_editrec', methods = ['POST'])
@login_required
def save_editrec():
    inputs = request.form

    fupdate = recommandations.query.get(inputs['id'])
    
    
    fupdate.titre           = inputs['titre']
    fupdate.description     = inputs['description']
    fupdate.domaine         = inputs['domaine']
    fupdate.specification   = inputs['specification']

    db.session.commit()
    flash("Recommandation Updated Successfully")

    return redirect(url_for('recommandation.list_recommandation'))
 
@recommandation.route('/recommandation/delete/<int:id>')
@login_required
def delete_rec(id):
    shit = recommandations.query.get(id)
    db.session.delete(shit)
    db.session.commit()
    flash("Recommandation Deleted Successfully")
    return redirect(url_for('recommandation.list_recommandation'))
    

  

    