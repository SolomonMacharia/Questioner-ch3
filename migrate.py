import os
import re
import psycopg2

db_url = psycopg2.connect("dbname='questioner_dev'")

def create_tables():
    print('connecting to db')
    conn = db_url
    cur = conn.cursor()
    tables = create_db_tables()

    for table in tables:
        cur.execute(table)
        conn.commit()

def drop_tables():
    '''Deletes all existing tables'''
    conn = db_url
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS users_table, meetups_table, questions_table, rsvps_table''')
    conn.commit()

def create_db_tables():
    users_table = '''CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(30) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        confirm_password VARCHAR(255) NOT NULL,
        registered VARCHAR(50),
        isAdmin BOOLEAN
    );'''

    meetups_table = '''CREATE TABLE IF NOT EXISTS meetups(
        id SERIAL PRIMARY KEY,
        created_on VARCHAR(50),
        location VARCHAR(255),
        images VARCHAR(255),
        topic VARCHAR(255),
        happening_on VARCHAR(25),
        tags VARCHAR(255)
    );'''

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

    rsvps_table = '''CREATE TABLE IF NOT EXISTS rsvps(
        id SERIAL PRIMARY KEY,
        meetupid INT NOT NULL,
        response VARCHAR(255)
    );'''

    tables = [users_table, meetups_table, questions_table, rsvps_table]
    return tables
