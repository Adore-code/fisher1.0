"""
 Created by Tang on 2020/2/11 12:35
"""
from datetime import timedelta

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

from app.models.book import db

login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds = 1)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先注册或登录'

    mail.init_app(app)

    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
