#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/7
"""配置"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    WTF_CSRF_CHECK_DEFAULT = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[SUBJECT]'
    MAIL_SENDER = 'MAIL Admin <mengyetxz@126.com>'
    MAIL_ADMIN = os.environ.get('MAIL_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
         'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}


# PORT = int(os.environ.get('PORT', '8000'))  # issue
# HOST = os.environ.get('HOST', '127.0.0.1')  # issue

# BCRYPT_LEVEL = 13  # 配置Flask-Bcrypt拓展
# MAIL_FROM_EMAIL = "my@example.com"  # 设置邮件来源


if __name__ == '__main__':
    pass
