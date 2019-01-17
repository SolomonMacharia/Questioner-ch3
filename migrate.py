import os
import psycopg2

url = psycopg2.connect(database='questioner_dev', password='', host='localhost', port='5432')
import pdb; pdb.set_trace()
print('Connected...')

def connect_db(url):
    print('wwwwwwww')
    conn = url
    return conn
def create_tables():
    print('qqq')
    import pdb; pdb.set_trace()
    conn = connect_db(url)
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
        registered DATE NOT NULL DEFAULT CURRENT_DATE,
        isAdmin BOOLEAN NOT NULL
    )''' 

    meetups_table = '''CREATE TABLE IF NOT EXISTS meetups(
        id SERIAL PRIMARY KEY,
        createdOn DATE NOT NULL DEFAULT CURRENT_DATE,
        location VARCHAR(255),
        images ,
        topic VARCHAR(255),
        happeningOn DATE NOT NULL CURRENT_DATE,
        tags VARCHR(255)
    )'''

    questions_table = '''CREATE TABLE IF NOT EXISTS questions(
        id SERIAL PRIMARY KEY,
        createdOn DATE NOT NULL CURRENT_DATE,
        createdBy INT NOT NULL,
        meetup INT NOT NULL,
        title VARCHAR(255),
        body VARCHAR(255),
        votes INT
    )'''

    rsvps_table = '''CREATE TABLE IF NOT EXISTS rsvps(
        id SERIAL PRIMARY KEY,
        meetup INT NOT NULL,
        user INT NOT NULL,
        response VARCHAR(255)
    )'''

    tables = [users_table, meetups_table, questions_table, rsvps_table]
    return tables

# create_tables()