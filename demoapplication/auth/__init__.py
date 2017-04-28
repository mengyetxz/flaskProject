#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/13
"""注册用户认证模块的蓝图"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

if __name__ == '__main__':
    pass
