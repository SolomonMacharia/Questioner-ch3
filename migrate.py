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
    host, port, db_name = re.match('postgres://(.*?):(.*?)/(.*)', database_url).groups()
    conn = psycopg2.connect("dbname={}".format(db_name))
    return conn

def create_tables():
    print('connecting to db')
    conn = db_connection(database_url)
    cur = conn.cursor()
    tables = create_db_tables()

    for table in tables:
        cur.execute(table)
        conn.commit()

def drop_tables():
    '''Deletes all existing tables'''
    conn = db_connection(database_url)
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS users_table, meetups_table, questions_table, rsvps_table''')
    conn.commit()
# Create tables


def create_db_tables():
    users_table = '''CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        u_id INT,
        username VARCHAR(30) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        confirm_password VARCHAR(255) NOT NULL,
        registered VARCHAR(50),
        isAdmin BOOLEAN
    );'''
    print("....users_table created")

    meetups_table = '''CREATE TABLE IF NOT EXISTS meetups(
        id SERIAL PRIMARY KEY,
        m_id INT,
        created_on VARCHAR(50),
        location VARCHAR(255),
        images VARCHAR(255),
        topic VARCHAR(255),
        happening_on VARCHAR(25),
        tags VARCHAR(255),

    );'''
    print("....meetups_table created ")

    questions_table = '''CREATE TABLE IF NOT EXISTS questions(
        id SERIAL PRIMARY KEY,
        meetupid INT REFERENCES meetups(id) ON DELETE CASCADE,
        created_on VARCHAR(50),
        created_by INT NOT NULL,
        meetup INT NOT NULL,
        title VARCHAR(255),
        body VARCHAR(255),
        votes INT

    );'''
    print("....questons_table created")

    rsvps_table = '''CREATE TABLE IF NOT EXISTS rsvps(
        id SERIAL PRIMARY KEY,
        meetupid INT NOT NULL,
        response VARCHAR(255)
    );'''
    print("....rsvp_tables created")

    tables = [users_table, meetups_table, questions_table, rsvps_table]
    return tables

# create_tables()
# drop_tables()
