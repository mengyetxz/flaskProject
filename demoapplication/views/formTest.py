#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""__DOC__"""

from flask import Blueprint, session, flash, redirect, render_template, url_for
from ..forms.forms import NameForm

formTest = Blueprint('formTest', __name__)


@formTest.route('/nameform', methods=['GET', 'POST'])
def form_test():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('look like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('form_test'))
    return render_template('formtest.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    pass
