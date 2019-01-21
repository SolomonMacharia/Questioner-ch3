from . import conn, cur
from flask import jsonify
from datetime import datetime
from psycopg2.extras import RealDictCursor

class Meetups:
    ''''This is the meetups model that aids in DB transactions''' 
    def __init__(self):
        pass

    def create_meetup(self,created_on,location, images, topic, happening_on):
        '''Adds a new meetup into the database'''
        cur.execute('''INSERT INTO meetups(created_on, location, images, topic, happening_on) VALUES(%s, %s, %s, %s, %s );''',\
                    (created_on, location, images, topic, happening_on))
        conn.commit()
    def get_all_meetups(self):
        """Fetches all meetups from the database"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id, location, images, topic, happening_on, tags FROM meetups ORDER BY id")
            rows = cur.fetchall()
            return rows