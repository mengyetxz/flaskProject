#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/8
"""__DOC__"""

import csv
import json
import os

from flask import render_template, redirect, url_for,\
    request, make_response, session, jsonify
from . import dashboard as dash
from .forms import QsForm
from ..path import CSV_PATH


@dash.route('/table')
def table():
    return render_template("dashboard/table.html")


@dash.route('/get_billing_data', methods=['GET'])
def get_billing_data():
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

    # response = make_response(json.dumps(data))
    # response.content_type = 'application/json'

    return jsonify(data)


@dash.route('/render_chart', methods=['GET', 'POST'])
def render_chart():
    form = QsForm()
    if form.validate_on_submit():
        session['qs'] = form.qs.data
        form.qs.data = ''
        return redirect(url_for('.render_chart'))
    return render_template('dashboard/echarts.html', form=form, qs=session.get('qs'))


@dash.route('/render_chart/addlist', methods=['GET', 'POST'])
def add_list():
    form = QsForm()
    if form.validate_on_submit():
        session['qs'] = form.qs.data
        form.qs.data = ''
        return redirect(url_for('.add_list'))
    return render_template('dashboard/addlist.html', form=form,
                           qs=request.args.get('qs') or session.get('qs'))


@dash.route('/get_linked_account_billing')
def get_linked_account_billing():
    data = dict()

    csv_dir = os.path.join(CSV_PATH, '412764460734-aws-cost-allocation-ACTS-2017-01.csv')
    with open(csv_dir, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        header = next(reader)
        # print header
        try:
            qs = request.args.get('qs')
            qs_index = header.index(qs)
            total_cost_index = header.index('TotalCost')
            account_id = request.args.get('account_id')
            account_id_index = header.index('LinkedAccountId')
            # print account_id
        except ValueError:
            return make_response()

        for row in reader:
            # print row[account_id_index]
            if row[account_id_index] == account_id:
                # print 'ok'
                if row[qs_index] in data.keys():
                    data[row[qs_index]] += float(row[total_cost_index])
                else:
                    if row[qs_index] == "":
                        data["Unknown"] = float(row[total_cost_index])
                    else:
                        # filter < 1
                        # if row[total_cost_index] >= '1':
                            data[row[qs_index]] = float(row[total_cost_index])
                # print data

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'

    return response


@dash.route('/render_chart/linked_account')
def render_chart_linked_account():
    return render_template('dashboard/echarts_account.html',
                           qs='ProductCode', account_id='425155429375')


if __name__ == '__main__':
    pass
