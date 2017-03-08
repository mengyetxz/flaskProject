from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from views import errorPages, login, testPages
from path import INS_PATH

app = Flask(__name__, instance_path=INS_PATH, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')  # issue

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

# import Blueprint
from views.views import index
app.register_blueprint(index)

from views.echartsTest import echartsTest
app.register_blueprint(echartsTest, url_prefix='/echarts-test')

from views.formTest import formTest
app.register_blueprint(formTest, url_prefix='/formtest')

from views.errorPages import error
app.register_blueprint(error, url_prefix='/error')

from views.testPages import test
app.register_blueprint(test, url_prefix='/test')

# Blueprint login test
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
    pass
