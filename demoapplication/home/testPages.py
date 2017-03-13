#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creaded on 2017/3/7
"""__DOC__"""

from datetime import datetime
from flask import render_template
import flask_excel as excel
from . import home


@home.route('/test')
def test_page():
    # qs = 'ProductCode'
    #return make_response(url_for('test_0', qs=qs))
    return render_template("testPages/test.html")


@home.route('/test/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())


@home.route('/test/bootstrap/<name>')
def boot(name):
    return render_template('bootstrap.html', name=name)


@home.route('/test/export')
def export_record():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv", file_name="./billing-data/export_csv.csv")

#@app.route('/datacsv')
#def data_csv():
#    csv_dir = os.path.join(CSV_PATH, '412764460734-aws-cost-allocation-ACTS-2017-01.csv')
#    f = open(csv_dir, 'r')
#    response = f.readlines()
#    f.close()
#    return response


#@app.route('data.csv')
#def output_csv():
#    output = StringIO()
#    some_dataframe.to_csv(output)

if __name__ == '__main__':
    pass
