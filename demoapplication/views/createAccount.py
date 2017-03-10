#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""__DOC__"""

import os
from flask import redirect, render_template, url_for, Blueprint, abort
from .. import db
from ..forms.forms import EmailPasswordForm
from ..util.security import ts, send_mail
from ..models import User

createAccount = Blueprint('createAccount', __name__)


@createAccount.route('/create', methods=['GET', 'POST'])
def create_account():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            _password=form.password.data
        )
        db.session.add(user)
        db.session.commit()

        # Now we'll send the email confirmation link
        subject = "Confirm your email"

        confirm_url = url_for(
            'confirm_email',
            token=token,
            _external=True
        )

        html = render_template(
            'mail/activate.html',
            confirm_url=confirm_url
        )

        send_mail(user.email, subject, html)

        return redirect(url_for('index'))
    return render_template("mail/create.html", form=form)


@createAccount.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = ts.loads(token, salt="email-confirm-key", max_age=86400)
    except:
        abort(404)

    user = User.query.filter_by(email=email).first_or_404()

    user.email_confirmed = True

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('signin'))

if __name__ == '__main__':
    pass
