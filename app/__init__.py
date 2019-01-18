from flask import Flask
from migrate import create_tables
from .api.v2 import version_two_bp


def create_app():
    app = Flask(__name__)
    create_tables()
    app.register(version_two_bp)
    return app
