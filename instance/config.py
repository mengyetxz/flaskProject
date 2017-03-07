#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/7
"""__DOC__"""

import os

DEBUG = True  # 启动Flask的Debug模式

# form SK
SECRET_KEY = os.urandom(24)

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\mengy\\PycharmProjects\\flaskProject\\SqliteTest.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True

if __name__ == '__main__':
    pass
