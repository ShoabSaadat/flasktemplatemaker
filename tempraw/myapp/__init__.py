import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from mainswitch import RunGuiVersion, RunWebVersion, GetApp, GetFolder

#Setup App------------------------------
template_folder = GetFolder('templates')
static_folder = GetFolder('static')
app = GetApp(__name__, template_folder, static_folder)

#Setup Form & Database------------------
isLive = False # True if for Heroku
if isLive:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
else:
    SECRET_KEY = 'MYSECRETKEY'
    dirpath = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(dirpath,'data.sqlite')

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

#Logins Configs------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

#BLUEPRINT REGISTRATION----------------
from myapp.core.views import core
from myapp.users.views import users
app.register_blueprint(core)
app.register_blueprint(users)
