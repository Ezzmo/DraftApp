from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n',
        'Email: ', self.email], '\r\n',
        'Name: ', self.first_name, ' ', self.last_name
        )

class Userteams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String(100), nullable=False, unique=True)
    player1 = db.Column(db.String(100), nullable=False)
    player2 = db.Column(db.String(100), nullable=False)
    player3 = db.Column(db.String(100), nullable=False)
    player4 = db.Column(db.String(100), nullable=False)
    player5 = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ', self.user_id, '\r\n',
            'Title: ', self.name, '\r\n'
        ])


class Players(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(4), nullable=False)









@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))