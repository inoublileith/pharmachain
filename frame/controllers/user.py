
from flask import  render_template, request, redirect, url_for, Blueprint,flash
from flask_login import login_required, current_user

from frame import db

from ..models.user import User

import datetime

user = Blueprint('user', __name__) #Moush nafs l esm maa l function besh mataamelsh error

@user.route('userlist')
@login_required
def list_user() :
    users = User.query.all()
    return render_template(user.html, users = users, user=current_user)


@user.route('view_adduser', methods=['GET'])
@login_required
def view_adduser():
    return render_template("adduser.html", user=current_user)
    


@user.route('save_adduser', methods=['POST'])
@login_required
def save_adduser():
    # default input
    etat = '1'
    profil = '1'
    tel = '0'
    permissions = '0'
    now = datetime.datetime.now()
    date_ins = now.strftime(" %d%m%Y" )
    date_upd = now.strftime(" %d%m%Y" )
    # Recuperation inputs from formulaire
    inputs = request.form
    first_name = inputs['nom']
    last_name = inputs['prenom']
    login = inputs['login']
    email = inputs['email']
    password = inputs['password']
    # table des parametres
    instance = User(first_name, last_name, email, login,  password, profil, tel, permissions, etat, date_upd, date_ins)
    db.session.add(instance)
    db.session.commit()
    #flash
    flash("User Inserted Successfully")
    return redirect(url_for('user.list_user'))
    


@user.route('view_edituser', methods=['GET'])
@login_required
def view_edituser():
    oneuser = User.query.get(request.args.get('id'))
    return render_template("edituser.html", oneuser=oneuser, user=current_user)



@user.route('save_edituser', methods=['POST'])
@login_required
def save_edituser():
    inputs = request.form
    fupdate = User.query.get(inputs['id'])
    fupdate.first_name = inputs['nom']
    fupdate.last_name = inputs['prenom']
    fupdate.login = inputs['login']
    fupdate.email = inputs['email']
    fupdate.password = inputs['password']
    db.session.commit()
    flash("User Updated Successfully")
    return redirect(url_for('user.list_user'))


@user.route('userdeleteintid')
@login_required
def delete_user(id):
    shit = User.query.get(id)
    db.session.delete(shit)
    db.session.commit()
    flash("User Deleted Successfully")
    return redirect(url_for('user.list_user'))
    
