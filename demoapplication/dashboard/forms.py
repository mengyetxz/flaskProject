#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""
提供QsForm ,用来获取查询字符串，
例如要按ProductCode查询：则输入ProductCode
要按LinkedAcountID查询：则输入LinkedAccountID
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


# test form
class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class QsForm(FlaskForm):
    qs = StringField('Please input query string:', validators=[DataRequired()])
    submit = SubmitField('Submit')


# test form
class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    pass
