from . import conn, cur
from psycopg2.extras import RealDictCursor


class QuestionModels(object):
    """Fetches all questions from the db"""
    def fetch_all_questions(self):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id, created_on, created_by, title, body, votes FROM questions ORDER BY votes")
            rows = cur.fetchall()
            return rows

