import csv
import json
import os
from datetime import datetime

import flask_excel as excel
from flask import Flask, render_template, redirect, \
    session, url_for, flash, request, make_response
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# ROOT_DIR = os.getcwd()  # same as above while cause an issue working on v
CSV_PATH = os.path.join(ROOT_DIR, 'billing-data')

INS_PATH = os.path.join(ROOT_DIR, 'instance')
app = Flask(__name__, instance_path=INS_PATH, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')  # issue

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class QsForm(FlaskForm):
    qs = StringField('Please input query string:', validators=[DataRequired()])
    submit = SubmitField('Submit')


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


from views.errorPages import error
app.register_blueprint(error, url_prefix='/error')

from views.testPages import test
app.register_blueprint(test, url_prefix='/test')

# login test
from views.login import login
app.register_blueprint(login, url_prefix='/login')

from flask_login import LoginManager
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = 'signin'


@loginManager.user_loader
def load_user(userid):
    return User.query.filter(User.id == userid).first()


if __name__ == '__main__':
    app.run()
