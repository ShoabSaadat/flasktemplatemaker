import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from mainswitch import RunGuiVersion, RunWebVersion, GetApp, GetFolder
from flask_mail import Mail

#Setup App------------------------------
template_folder = GetFolder('templates')
static_folder = GetFolder('static')
app = GetApp(__name__, template_folder, static_folder)
from hashing import GetUnhashed, GetHashed

#Setup Form & Database------------------
isOffline = True # False if for Heroku
if isOffline:
    SECRET_KEY = 'MYSECRETKEY'
    dirpath = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(dirpath,'data.sqlite')
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

#Logins Configs------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

#Setup Mail------------------------------
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
if isOffline:
    app.config['MAIL_USERNAME'] = GetUnhashed('0&15&15&24&22&7&4&4&11&82&22&4&1&12&0&18&19&4&17&80&6&12&0&8&11&82&2&14&12')
    app.config['MAIL_PASSWORD'] = GetUnhashed('33&20&18&18&80&52&13&32&40&0&22')
else:
    app.config['MAIL_SERVER'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_SERVER'] = os.environ.get('MAIL_PASSWORD')
mail = Mail(app)

#Blueprint Registeration----------------
from myapp.core.views import core
from myapp.users.views import users
from myapp.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
