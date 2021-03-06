from . import conn, cur
from flask import jsonify, abort
from datetime import datetime
from psycopg2.extras import RealDictCursor


class Meetups:
    ''''This is the meetups model that aids in DB transactions'''

    def __init__(self):
        self.created_on = datetime.now()
        pass

    def create_meetup(self, location, images, topic, happening_on, current_user):
        '''Adds a new meetup into the database'''
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute('''INSERT INTO meetups(created_on, location, images, topic, happening_on, created_by) VALUES(%s, %s, %s, %s, %s, %s) RETURNING *;''',
                        (self.created_on, location, images, topic, happening_on, current_user))
            created_meetup = cur.fetchone()
            conn.commit()
            return created_meetup

    def get_all_meetups(self):
        """Fetches all meetups from the database"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT id, created_on, location, images, topic, happening_on FROM meetups ORDER BY id")
            rows = cur.fetchall()
            return rows

    def get_one_meetup(self, id):
        """Fetches a single meetup from the db based on it's id"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT id, created_on, location, images, topic, happening_on FROM meetups WHERE id = {}".format(id))
            rows = cur.fetchone()
            return rows

    def delete_meetup(self, id):
        """This methods deletes a meetup from the db based on the its id number."""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "DELETE FROM meetups WHERE id = {} RETURNING *".format(id))
            deleted = cur.fetchone()
            conn.commit()
            return deleted
