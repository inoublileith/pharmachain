
from flask import  render_template, Blueprint
from flask_login import login_required, current_user


routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
   return render_template("login.html")

@routes.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)


