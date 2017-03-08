#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""__DOC__"""

import os

APP_DIR = os.path.dirname(os.path.abspath(__file__))
# ROOT_DIR = os.getcwd()  # same as above while cause an issue working on venv
CSV_PATH = os.path.join(APP_DIR, 'billing-data')

INS_PATH = os.path.join(APP_DIR, '../', 'instance')


if __name__ == '__main__':
    pass
