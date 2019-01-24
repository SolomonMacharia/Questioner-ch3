from . import cur, conn
from psycopg2.extras import RealDictCursor
from datetime import datetime
from functools import wraps
from app import config
import jwt

class Users:
    def __init__(self):
        pass

    def create_user(self, username, email, password, confirm_password):
        cur.execute('''INSERT INTO users(username, email, password, confirm_password) VALUES(%s, %s, %s, %s );''',\
         (username, email, password, confirm_password))
        conn.commit()

    def get_all_user(self):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id, username, email FROM users ORDER BY id" )
            rows = cur.fetchall()
            return rows

    def get_single_user(self, id):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT username, email FROM users WHERE id = {}".format(id) )
            rows = cur.fetchone()
            return rows
    
    def get_user_by_username(self, username):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM users WHERE username = %s;", (username,))
            rows = cur.fetchone()
            return rows

