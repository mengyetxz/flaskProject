#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""
测试，无实际使用
"""

# from itsdangerous import URLSafeTimedSerializer
# from .. import mail
# from flask_mail import Message
# from flask import render_template
# from threading import Thread
#
# ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])
#
#
# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)
#
#
# def send_email(to, subject, template, **kwargs):
#     msg = Message(app.config('MAIL_SUBJECT_PREFIX') + subject,
#                   sender=app.config('MAIL_SENDER'),
#                   recipients=[to])
#     msg.body = render_template(template, '.txt', **kwargs)
#     msg.html = render_template(template, '.html', **kwargs)
#     thr = Thread(target=send_async_email, args=[app, msg])
#     thr.start()
#     return thr
#
#
# if __name__ == '__main__':
#     pass
