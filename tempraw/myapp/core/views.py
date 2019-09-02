from flask import Blueprint, render_template
core = Blueprint('core', __name__)

@core.route('/')
def home():
    return render_template('home.html')

@core.route('/info')
def info():
    return render_template('info.html')
