from . import conn, cur
from psycopg2.extras import RealDictCursor
from datetime import datetime


class QuestionModels(object):
    def __init__(self):
        self.created_on = datetime.now()

    def create_question(self, title, body, votes):
        cur.execute('''INSERT INTO questions(created_on, title, body, votes) VALUES(%s, %s, %s, %s );''',\
                    (self.created_on, title, body, votes))
        conn.commit()
    
    def fetch_all_questions(self):
        """Fetches all questions from the db"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id, created_on, title, body, votes FROM questions ORDER BY votes")
            rows = cur.fetchall()
            return rows

