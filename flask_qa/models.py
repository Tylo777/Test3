from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from .extensions import db 

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(100))
    appd = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)
