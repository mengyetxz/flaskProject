#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/10
"""__DOC__"""

from flask import Blueprint

dashboard = Blueprint('dashboard', __name__)

from . import views

if __name__ == '__main__':
    pass
