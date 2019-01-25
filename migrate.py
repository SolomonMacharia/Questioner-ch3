import os
import re
import psycopg2

environment = os.getenv('APP_ENV')
database_url = None

if environment == 'production':
    database_url = os.getenv('DATABASE_URL')

if environment == 'development':
    database_url = os.getenv('DEV_DATABASE_URL')

if environment == 'testing':
    database_url = os.getenv('TEST_DATABASE_URL')


def db_connection(database_url):
    host, port, db_name = re.match(
        'postgres://(.*?):(.*?)/(.*)', database_url).groups()
    conn = psycopg2.connect("dbname={}".format(db_name))
    return conn


def create_tables():
    print('connecting to db')
    conn = db_connection(database_url)
    cur = conn.cursor()
    tables = create_db_tables()

    tables_names = ['users', 'meetups', 'questions', 'rsvps']
    current_table = 0
    for table in tables:
        cur.execute(table)
        conn.commit()
        print("...{} created".format(tables_names[current_table]))
        current_table += 1


def drop_tables():
    '''Deletes all existing tables'''
    conn = db_connection(database_url)
    cur = conn.cursor()
    cur.execute(
        '''DROP TABLE IF EXISTS rsvps, questions, meetups, users''')
    conn.commit()


def create_db_tables():
    users_table = '''CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(30) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        confirm_password VARCHAR(255) NOT NULL,
        registered VARCHAR(50),
        isAdmin BOOLEAN
    );'''

    meetups_table = '''CREATE TABLE IF NOT EXISTS meetups(
        id SERIAL PRIMARY KEY,
        created_on VARCHAR(50),
        created_by INTEGER NOT NULL REFERENCES users (id),
        location VARCHAR(255),
        images VARCHAR(255),
        topic VARCHAR(255),
        happening_on VARCHAR(25)
    );'''
    # print("....meetups_table created ")

    questions_table = '''CREATE TABLE IF NOT EXISTS questions(
        id SERIAL PRIMARY KEY,
        created_by INTEGER NOT NULL REFERENCES users (id),
        meetup_id INTEGER NOT NULL REFERENCES meetups (id),
        created_on VARCHAR(50),
        title VARCHAR(255),
        body VARCHAR(255),
        votes INT DEFAULT 0
    );'''

    rsvps_table = '''CREATE TABLE IF NOT EXISTS rsvps(
        id SERIAL PRIMARY KEY,
        meetupid INT NOT NULL,
        response VARCHAR(255)

    );'''

    tables = [users_table, meetups_table, questions_table, rsvps_table]
    return tables
