from flask import  Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from myapp.users.forms import LoginForm, RegisterForm
from myapp.models import UserModel
from myapp import db
users = Blueprint('users', __name__)

@users.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserModel.query.filter_by(username=form.username.data).first()
        if user is not None:
            if user.CheckPassword(form.password.data):
                login_user(user)

                next = request.args.get('next')
                if next == None or not next[0] == '/':
                    next = url_for('users.dashboard')
                return redirect(next)

    return render_template('login.html', form=form)

@users.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('core.home'))

@users.route('/register', methods=['GET','POST'])
def register():
    UserAlreadyRegistered = False
    form = RegisterForm()
    if form.validate_on_submit():
        if form.email_unique(form.username.data) and form.username_unique(form.email.data):
            registeringUser = UserModel(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(registeringUser)
            db.session.commit()
            return redirect(url_for('users.login')) #Why not login directly
        else:
            flash('Your username or email has already been registered. Try a different one or login.')
            UserAlreadyRegistered = True
            return render_template('register.html', form=form, UserAlreadyRegistered=UserAlreadyRegistered)
    return render_template('register.html', form=form, UserAlreadyRegistered=UserAlreadyRegistered)

@users.route('/dashboard', methods=['POST','GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')
