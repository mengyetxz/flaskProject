#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/7
"""__DOC__"""

from flask import render_template
from . import home


@home.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@home.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    pass
