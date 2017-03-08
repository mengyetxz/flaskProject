#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""__DOC__"""

from flask import Blueprint, render_template
index = Blueprint('index', __name__)


@index.route('/', methods=['GET'])
def _index():
    return render_template('index.html')

if __name__ == '__main__':
    pass
