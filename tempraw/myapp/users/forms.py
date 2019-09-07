from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, FileField, ValidationError, SelectField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo
from myapp.models import UserModel

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submitBtn = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('rep_password',message='Passwords must match...')])
    rep_password = PasswordField('Repeat Password', validators=[DataRequired()])
    submitBtn = SubmitField('Register')

    def email_unique(self, field):
        if UserModel.query.filter_by(email=field).first():
            return False
        else:
            return True

    def username_unique(self, field):
        if UserModel.query.filter_by(username=field).first():
            return False
        else:
            return True


##--------------------------

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
              Email()] )
    submitBtn = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()] )
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match...')])
    submitBtn = SubmitField('Reset Password')
