from flask import render_template, request, redirect, url_for, Blueprint,flash
from werkzeug.security import generate_password_hash, check_password_hash
#import MySQLdb.cursors


from flask_login import login_user, login_required, logout_user, current_user
from ..models.user import User
from frame import db


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # login = request.form.get('var') -> var ylzem nafs l esm ly fy name fel html !!!
        login = request.form.get('username')
        password = request.form.get('password')

        account = User.query.filter_by(login=login).first()
        
        if account:
            if check_password_hash(account.password, password):
                flash('Logged in successfully!')
                login_user(account, remember=True)
                return redirect(url_for('routes.home'))
            else:
                flash('Incorrect entry, try again.')
        else:
            flash('Account does not exist.')

    return render_template("login.html")



@auth.route('/register', methods=['GET', 'POST'])
def register():
    
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form :
        # Create variables for easy access
        profil = 1
        nom = request.form['nom']
        login = request.form['username']
        password = request.form['password']
        #password = generate_password_hash(request.form['password'])
        # Check if account exists using MySQL
        account = User.query.filter_by(login=login).first()
        # If account exists show error and validation checks
        if account:
           flash('Account already exists!')
        else:

        # Account doesnt exists and the form data is valid, now insert new account into accounts table
       
   

            new_User = User(nom=nom, prenom='', tel='0', email='', adresse='',  cpostal='0', gouvernorat='', login=login, password=generate_password_hash(password, method='sha256'), profil=profil, permissions='0', avatar='',  date_ins='', date_upd='', etat='0')

            db.session.add(new_User)
            db.session.commit()
            login_user(new_User, remember=True)
            flash('Account created!')
            return redirect(url_for('routes.home'))
    elif request.method == 'POST':
        flash('Please fill out the form!')
    
    # Show registration form with message (if any)
    return render_template('register.html')
 
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))