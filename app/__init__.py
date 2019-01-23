import os
from flask import Flask
from .api.v2 import version_two_bp
from instance.config import app_settings
from migrate import create_tables

def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    create_tables()
    app.config.from_object(app_settings[config])
    app.register_blueprint(version_two_bp)
    return app
