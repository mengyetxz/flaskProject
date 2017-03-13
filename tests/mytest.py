#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/10
"""__DOC__"""

import unittest
from flask import current_app
from demoapplication import create_app, db


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exist(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

if __name__ == '__main__':
    pass
