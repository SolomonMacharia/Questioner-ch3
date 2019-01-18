import os
import psycopg2

url = psycopg2.connect(database='questioner_dev',
                       password='', host='localhost', port='5432')


def connect_db(url):
    conn = url
    return conn


def create_tables():
    conn = connect_db(url)
    curr = conn.cursor()
    tables = create_db_tables()

    for table in tables:
        curr.execute(table)
    conn.commit()

# Create tables


def create_db_tables():
    users_table = '''CREATE TABLE IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(30) NOT NULL UNIQUE,
        email VARCHAR(255) NOT NULL UNIQUE,
        registered DATE NOT NULL DEFAULT NOW(),
        isAdmin BOOLEAN NOT NULL
    )'''

    meetups_table = '''CREATE TABLE IF NOT EXISTS meetups(
        meetups_id SERIAL PRIMARY KEY,
        createdOn DATE NOT NULL DEFAULT NOW(),
        location VARCHAR(255),
        images VARCHAR(255),
        topic VARCHAR(255),
        happeningOn DATE NOT NULL DEFAULT NOW(),
        tags VARCHAR(255)
    )'''

    questions_table = '''CREATE TABLE IF NOT EXISTS questions(
        question_id SERIAL PRIMARY KEY,
        createdOn DATE NOT NULL DEFAULT NOW(),
        createdBy INT NOT NULL,
        meetup INT NOT NULL,
        title VARCHAR(255),
        body VARCHAR(255),
        votes INT
    )'''

    rsvps_table = '''CREATE TABLE IF NOT EXISTS rsvps(
        rsvp_id SERIAL PRIMARY KEY,
        meetupid INT NOT NULL,
        response VARCHAR(255),
        userid INT NOT NULL
    )'''

    tables = [users_table, meetups_table, questions_table, rsvps_table]
    return tables

# create_tables()
