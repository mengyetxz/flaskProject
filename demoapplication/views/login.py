#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/7
"""__DOC__"""

from flask import Blueprint, render_template, redirect, url_for
login = Blueprint('login', __name__)
from ..forms.forms import EmailPasswordForm


@login.route('/', methods=['GET', 'POST'])
def login_fun():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


if __name__ == '__main__':
    pass
