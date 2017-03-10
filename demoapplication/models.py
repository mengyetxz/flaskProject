#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/7
"""__DOC__"""

from . import db
from sqlalchemy.ext.hybrid import hybrid_property
from . import bcrypt


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.role


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True)
    _password = db.Column(db.String(128))
    roleId = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, username, email, _password):
        self.username = username
        self.email = email
        self._password = _password

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    pass
