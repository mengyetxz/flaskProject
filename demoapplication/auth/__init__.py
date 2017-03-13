#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/13
"""__DOC__"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

if __name__ == '__main__':
    pass
