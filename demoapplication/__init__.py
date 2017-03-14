from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .path import INS_PATH
# from flask_bcrypt import Bcrypt
from config import config
# from home import errors, login, testPages

# app = Flask(__name__, instance_path=INS_PATH, instance_relative_config=True)
# app.config.from_object('config')
# app.config.from_pyfile('config.py')  # issue

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
# bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .dashboard import dashboard as dash_blueprint
    app.register_blueprint(dash_blueprint, url_prefix='/dash')

    return app

if __name__ == '__main__':
    pass
