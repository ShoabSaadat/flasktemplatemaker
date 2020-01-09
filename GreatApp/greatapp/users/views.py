from flask import  Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from greatapp.users.forms import LoginForm, RegisterForm, RequestResetForm, ResetPasswordForm
from greatapp.models import UserModel
from greatapp import db, mail
import ast
from flask import jsonify
##--
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_mail import Message
from werkzeug import generate_password_hash, check_password_hash


#Defining its Blueprint------------
users = Blueprint('users', __name__)

#Main Routes----------------------------------
@users.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))

    UserExistsError = False
    UserPasswordError = False
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
            else:
                UserPasswordError = True
                return render_template('login.html', form=form, UserPasswordError=UserPasswordError)
        else:
            UserExistsError = True
            return render_template('login.html', form=form, UserExistsError=UserExistsError)

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
        if form.email_unique(form.email.data) and form.username_unique(form.username.data):
            registeringUser = UserModel(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(registeringUser)
            db.session.commit()
            return redirect(url_for('users.login')) #Why not login directly
        else:
            UserAlreadyRegistered = True
            return render_template('register.html', form=form, UserAlreadyRegistered=UserAlreadyRegistered)
    return render_template('register.html', form=form, UserAlreadyRegistered=UserAlreadyRegistered)

@users.route('/ajaxhandle', methods=['POST', 'GET'])
@login_required
def ajaxhandle():
    sentTerm = ''
    testVar = []
    if request.get_json().get('sentTerm') != '' and request.get_json().get('sentTerm') != None:
        oldSentTerm = request.get_json().get('sentTerm')#I am not using it
        testVar = request.get_json().get('testVar')
        sentTerm = str('New term is: '+testVar[0])
    packet = {'sentTerm':sentTerm, 'testVar': testVar}
    print('packet: ', packet)
    if request.get_json().get('trigger') == 'test':
        return jsonify({'url': url_for('users.dashboard',packet=packet)})

@users.route('/dashboard', methods=['POST','GET'])
@login_required
def dashboard():
    sentTerm = 'default'
    if request.args.get('packet') != '' and request.args.get('packet') != None:
        packet = request.args.get('packet')
        packet=ast.literal_eval(packet)
        sentTerm=packet['sentTerm']
        testVar=packet['testVar']
        print('Sent test var from dashboard.html was: ', testVar)
    return render_template('dashboard.html', sentTerm=sentTerm)

##-------
def SendResetEmail(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='appywheel.webmaster@gmail.com', recipients=[user.email])
    msg.body = f''' To reset your password visit the following link :
{url_for('users.reset_token', token = token, _external=True)}

If you did not make this request, kindly ignore this email.
'''
    mail.send(msg)

@users.route('/reset_password', methods=('GET', 'POST',))
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))

    form = RequestResetForm()
    if form.validate_on_submit():
        email = form.email.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            SendResetEmail(user)
            flash('You will receive an email soon at the provided email address if found in our system', 'info')
            return redirect(url_for('users.login'))
        else:
            flash('You will receive an email soon at the provided email address if found in our system', 'info')
    return render_template('reset_request.html', form=form)

@users.route('/reset_password/<token>', methods=('GET', 'POST',))
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))

    user = UserModel.verify_reset_token(token)
    if not user:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.password_hash = generate_password_hash(form.password.data)
        db.session.commit()
        flash('You password has been updated', 'info')
        return redirect(url_for('users.login')) #Why not login directly
    return render_template('reset_token.html', form=form)
