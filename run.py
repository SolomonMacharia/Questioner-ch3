import os
import re
import psycopg2

from app import create_app

environment = os.getenv('APP_ENV')

app = create_app(environment)
