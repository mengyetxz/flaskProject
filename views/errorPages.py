#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/7
"""__DOC__"""

from flask import Blueprint, render_template

error = Blueprint('error', __name__)


@error.errorhandler(404)
def page_not_found(e):
    return render_template('errorPages/404.html'), 404


@error.errorhandler(500)
def internal_server_error(e):
    return render_template('errorPages/500.html'), 500


if __name__ == '__main__':
    pass
