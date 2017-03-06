from flask import Flask, render_template, redirect, \
    session, url_for, flash, request, make_response, \
    jsonify
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import json
import csv
import os
import flask_excel as excel
from StringIO import StringIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(ROOT_DIR, 'billing-data')

bootstrap = Bootstrap(app)

moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class QsForm(FlaskForm):
    qs = StringField('Please input query string:', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/nameform', methods=['GET', 'POST'])
def formtest():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('look like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('formtest'))
    return render_template('formtest.html', form=form, name=session.get('name'))


@app.route('/user/<name>')
def user(name):

    return render_template('user.html', name=name, current_time=datetime.utcnow())


@app.route('/bootstrap/<name>')
def boot(name):
    return render_template('bootstrap.html', name=name)


@app.route('/test_0', methods=['GET'])
def test_0():
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


@app.route('/test_1/echarts-test', methods=['GET', 'POST'])
def test_1():
    form = QsForm()
    if form.validate_on_submit():
        session['qs'] = form.qs.data
        form.qs.data = ''
        return redirect(url_for('test_1'))
    return render_template('echarts-test.html', form=form, qs=session.get('qs'))


@app.route('/addlist', methods=['GET', 'POST'])
def test_2():
    form = QsForm()
    if form.validate_on_submit():
        session['qs'] = form.qs.data
        form.qs.data = ''
        return redirect(url_for('test_2'))
    return render_template('addlist.html', form=form, qs=request.args.get('qs'))


@app.route('/t')
def t():
    # qs = 'ProductCode'
    #return make_response(url_for('test_0', qs=qs))
    return render_template("test.html")


@app.route('/table')
def table():
    return render_template("table.html")


#@app.route('/datacsv')
#def data_csv():
#    csv_dir = os.path.join(CSV_PATH, '412764460734-aws-cost-allocation-ACTS-2017-01.csv')
#    f = open(csv_dir, 'r')
#    response = f.readlines()
#    f.close()
#    return response


@app.route('/export')
def export_record():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv", file_name="./billing-data/export_csv.csv")


#@app.route('data.csv')
#def output_csv():
#    output = StringIO()
#    some_dataframe.to_csv(output)





if __name__ == '__main__':
    app.run(debug=True)
