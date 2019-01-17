from flask import Flask
from migrate import create_tables

create_tables()



def create_app():
    app = Flask(__name__)
    return app