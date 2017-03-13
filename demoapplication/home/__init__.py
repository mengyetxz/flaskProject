#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/7
"""__DOC__"""

from flask import Blueprint

home = Blueprint('home', __name__)

from . import views

if __name__ == '__main__':
    pass
