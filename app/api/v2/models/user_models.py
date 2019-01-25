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
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute('''INSERT INTO users(username, email, password, confirm_password) VALUES(%s, %s, %s, %s ) RETURNING username, email;''',
                        (username, email, password, confirm_password))
            created_user = cur.fetchone()
            conn.commit()
            cur.execute('ROLLBACK')

            return created_user

    def get_all_user(self):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id, username, email FROM users ORDER BY id")
            rows = cur.fetchall()
            return rows

    def get_single_user(self, id):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT username, email FROM users WHERE id = {}".format(id))
            rows = cur.fetchone()
            return rows

    def get_user_by_email(self, email):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:

            email_parameter = "\'{}\'".format(email)
            query = 'SELECT * from users where email = {}'.format(
                email_parameter)
            cur.execute(query)
            rows = cur.fetchone()
            return rows
