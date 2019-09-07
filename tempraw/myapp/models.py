from myapp import db, login_manager, app
from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin
#--
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)


class UserModel(db.Model, UserMixin):
    __tablename__ = 'usermodel'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(64), nullable=False, index=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password):
        self.username =username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f'Username is {self.username} with an email address of {self.email}.'

    def CheckPassword(self, password):
        return check_password_hash(self.password_hash, password)

    ##-----------
    def get_reset_token(self, expiration=1800):
        s = Serializer(app.config['SECRET_KEY'], expiration)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        id = data.get('user_id')
        if id:
            return UserModel.query.get(id)
        return None
