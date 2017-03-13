#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""__DOC__"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class QsForm(FlaskForm):
    qs = StringField('Please input query string:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    pass
