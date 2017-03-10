#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""__DOC__"""

from flask import Blueprint, session, flash, redirect, render_template, url_for
from ..forms.forms import NameForm
from ..models import User
from .. import db, app
from ..util.security import send_email

formTest = Blueprint('formTest', __name__)


@formTest.route('/nameform', methods=['GET', 'POST'])
def form_test():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['MAIL_ADMIN']:
                send_email(app.config('MAIL_ADMIN'), 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('formTest.form_test'))
    return render_template('testPages/formtest.html', form=form, name=session.get('name'),
                           known=session.get('known', False))


if __name__ == '__main__':
    pass
