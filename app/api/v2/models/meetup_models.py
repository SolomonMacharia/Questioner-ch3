from . import conn, cur
from datetime import datetime

class Meetups:
    ''''This is the meetups model that aids in DB transactions''' 
    def __init__(self):
        pass

    def create_meetup(self,created_on,location, images, topic, happening_on):
        '''Adds a new meetup into the database'''
        cur.execute('''INSERT INTO meetups(created_on, location, images, topic, happening_on) VALUES(%s, %s, %s, %s, %s );''',\
                    (created_on, location, images, topic, happening_on))
        conn.commit()
