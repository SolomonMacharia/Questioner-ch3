import os
from flask import Flask
from migrate import create_tables
from .api.v2 import version_two_bp
from app import config


def create_app(app_settings='development'):
    app = Flask(__name__)
    app.config.from_object(config.APP_SETTINGS[app_settings])
    app.register_blueprint(version_two_bp)
    return app
