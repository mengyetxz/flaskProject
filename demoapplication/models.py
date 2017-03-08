#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/7
"""__DOC__"""

from . import db


class Engine(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    thrust = db.Column(db.Integer, default=0)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

# ------------------TESTTTTTTTTTTTTTT-------------------
from . import app
from flask_login import LoginManager
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = 'signin'


@loginManager.user_loader
def load_user(userid):
    return User.query.filter(User.id == userid).first()

if __name__ == '__main__':
    pass
