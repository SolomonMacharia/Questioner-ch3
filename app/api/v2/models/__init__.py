import os
from migrate import db_connection

environment = os.getenv('APP_ENV')
database_url = None

if environment == 'production':
    database_url = os.getenv('DATABASE_URL')

if environment == 'development':
    database_url = os.getenv('DEV_DATABASE_URL')

if environment == 'testing':
    database_url = os.getenv('TEST_DATABASE_URL')

conn = db_connection(database_url)
cur = conn.cursor()