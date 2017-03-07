#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/7
"""__DOC__"""

from flask import Blueprint, render_template

test = Blueprint('test', __name__)


@test.route('/')
def test_page():
    # qs = 'ProductCode'
    #return make_response(url_for('test_0', qs=qs))
    return render_template("testPages/test.html")


if __name__ == '__main__':
    pass
