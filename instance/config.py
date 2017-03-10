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
SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 每次请求结束后 自动提交数据库中的变动
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True

# flask-mail
MAIL_SERVER = 'smtp.126.com'
MAIL_ADMIN = 'mengyetxz@126.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
# mail-header-body
MAIL_SUBJECT_PREFIX = '[SUBJECT]'
MAIL_SENDER = 'Admin mengyetxz@126.com'

if __name__ == '__main__':
    pass
