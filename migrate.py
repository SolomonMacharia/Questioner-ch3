import os
import psycopg2

db_connection = psycopg2.connect("dbname='questioner_dev'")

def create_tables():
    print('connecting to db')
    conn = db_connection
    curr = conn.cursor()
    tables = create_db_tables()

    for table in tables:
        curr.execute(table)
    conn.commit()

# Create tables


def create_db_tables():
    users_table = '''CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(30) NOT NULL UNIQUE,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        confirmPassword VARCHAR(255) NOT NULL,
        registered DATE NOT NULL DEFAULT NOW(),
        isAdmin BOOLEAN
    )'''
    print("....users_table created")

    meetups_table = '''CREATE TABLE IF NOT EXISTS meetups(
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        createdOn DATE NOT NULL DEFAULT NOW(),
        location VARCHAR(255),
        images VARCHAR(255),
        topic VARCHAR(255),
        happeningOn DATE NOT NULL DEFAULT NOW(),
        tags VARCHAR(255)
    )'''
    print("....meetups_table created ")

    questions_table = '''CREATE TABLE IF NOT EXISTS questions(
        id SERIAL PRIMARY KEY,
        meetup_id INT REFERENCES meetups(id) ON DELETE CASCADE,
        user_id INT REFERENCES users(id),
        createdOn DATE NOT NULL DEFAULT NOW(),
        createdBy INT NOT NULL,
        meetup INT NOT NULL,
        title VARCHAR(255),
        body VARCHAR(255),
        votes INT

    )'''
    print("....questons_table created")

    rsvps_table = '''CREATE TABLE IF NOT EXISTS rsvps(
        id SERIAL PRIMARY KEY,
        meetup_id INT REFERENCES meetups(id) ON DELETE CASCADE,
        user_id INT REFERENCES users(id),
        meetupid INT NOT NULL,
        response VARCHAR(255),
        userid INT NOT NULL
    )'''
    print("....rsvp_tables created")

    tables = [users_table, meetups_table, questions_table, rsvps_table]
    return tables

create_tables()
