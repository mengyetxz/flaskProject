#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""__DOC__"""

from flask import render_template, redirect, url_for, abort, session
# from .forms import EmailPasswordForm, NameForm
from . import home
# from .. import db
# from ..models import User
# from ..util.security import ts, send_email


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/test')
def test():
    return render_template('silder-menu.html')

# @home.route('/', methods=['GET'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             session['known'] = False
#             if app.config['MAIL_ADMIN']:
#                 send_email(app.config('MAIL_ADMIN'), 'New User',
#                            'mail/new_user', user=user)
#         else:
#             session['known'] = True
#         session['name'] = form.name.data
#         form.name.data = ''
#         return redirect(url_for('formTest.form_test'))
#     return render_template('testPages/formtest.html', form=form, name=session.get('name'),
#                            known=session.get('known', False))
#
#
# @home.route('/login', methods=['GET', 'POST'])
# def login():
#     form = EmailPasswordForm()
#     if form.validate_on_submit():
#         return redirect(url_for('.index'))
#     return render_template('login.html', form=form)
#
#
# @home.route('/signin', methods=['GET', 'POST'])
# def sign_in():
#     pass
#
#
# @home.route('/signup', methods=['GET', 'POST'])
# def create_account():
#     form = EmailPasswordForm()
#     if form.validate_on_submit():
#         user = User(
#             email=form.email.data,
#             username=username,
#             _password=form.password.data
#         )
#         db.session.add(user)
#         db.session.commit()
#
#         # Now we'll send the email confirmation link
#         subject = "Confirm your email"
#
#         confirm_url = url_for(
#             'confirm_email',
#             token=token,
#             _external=True
#         )
#
#         html = render_template(
#             'mail/activate.html',
#             confirm_url=confirm_url
#         )
#
#         send_email(user.email, subject, html)
#
#         return redirect(url_for('index'))
#     return render_template("mail/create.html", form=form)
#
#
# @home.route('/confirm/<token>')
# def confirm_email(token):
#     try:
#         email = ts.loads(token, salt="email-confirm-key", max_age=86400)
#     except:
#         abort(404)
#
#     user = User.query.filter_by(email=email).first_or_404()
#
#     user.email_confirmed = True
#
#     db.session.add(user)
#     db.session.commit()
#
#     return redirect(url_for('.sign_in'))

if __name__ == '__main__':
    pass
