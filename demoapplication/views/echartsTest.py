#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""__DOC__"""

import os
import csv
import json
from flask import Blueprint, render_template, redirect, url_for,\
    request, make_response, session
from ..forms.forms import QsForm
from ..path import CSV_PATH

echartsTest = Blueprint('echartsTest', __name__)


@echartsTest.route('/getdata', methods=['GET'])
def get_data():
    data = dict()

    csv_dir = os.path.join(CSV_PATH, '412764460734-aws-cost-allocation-ACTS-2017-01.csv')
    with open(csv_dir, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        header = next(reader)
        try:
            qs = request.args.get('qs')
            qs_index = header.index(qs)
            total_cost_index = header.index('TotalCost')
        except ValueError:

            return make_response()

        for row in reader:
            if row[qs_index] in data.keys():
                data[row[qs_index]] += float(row[total_cost_index])
            else:
                if row[qs_index] == "":
                    data["Unknown"] = float(row[total_cost_index])
                else:
                    data[row[qs_index]] = float(row[total_cost_index])

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'

    return response


# BuildError: Could not build url for endpoint 'test_1'.
# Did you mean 'echartsTest.test_1' instead?
@echartsTest.route('/', methods=['GET', 'POST'])
def test_1():
    form = QsForm()
    if form.validate_on_submit():
        session['qs'] = form.qs.data
        form.qs.data = ''
        return redirect(url_for('echartsTest.test_1'))
    return render_template('echarts-test.html', form=form, qs=session.get('qs'))


@echartsTest.route('/addlist', methods=['GET', 'POST'])
def test_2():
    form = QsForm()
    if form.validate_on_submit():
        session['qs'] = form.qs.data
        form.qs.data = ''
        return redirect(url_for('test_2'))
    return render_template('addlist.html', form=form, qs=request.args.get('qs'))


@echartsTest.route('/table')
def table():
    return render_template("table.html")


if __name__ == '__main__':
    pass
