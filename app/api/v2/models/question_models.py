from . import conn, cur
from psycopg2.extras import RealDictCursor
from datetime import datetime


class QuestionModels(object):
    def __init__(self):
        self.created_on = datetime.now()

    def create_question(self, title, body, meetup_id, current_user):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute('''INSERT INTO questions(title, body, meetup_id, created_by, created_on) VALUES(%s, %s, %s, %s, %s) RETURNING *;''',
                        (title, body, meetup_id, current_user, self.created_on))
            created_question = cur.fetchone()
            conn.commit()
            return created_question

    def fetch_all_questions(self):
        """Fetches all questions from the db"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                '''
                    SELECT questions.id, questions.created_on, questions.title,
                        questions.body, questions.votes, (users.id, users.username, users.email) as created_by
                    FROM questions
                    INNER JOIN users
                    ON questions.created_by = users.id
                    ORDER BY questions.votes DESC
                ''')
            rows = cur.fetchall()
            return rows

    def upvote_question(self, id):
        """Updates votes"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT votes FROM questions WHERE id = {}".format(id))
            data = cur.fetchone()

            if not data:
                return {'Message': 'Question {} doesnt exist'.format(id)}

            vote = data['votes'] + 1

            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    "UPDATE questions SET votes = %s WHERE id = %s RETURNING *", (vote, id))
                upvoted_question = cur.fetchone()
                conn.commit()
                return upvoted_question

    def downvote_question(self, id):
        """Updates votes"""
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT votes FROM questions WHERE id = {}".format(id))
            data = cur.fetchone()

            if not data:
                return {'Message': 'Question {} doesnt exist'.format(id)}

            vote = data['votes'] - 1

            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    "UPDATE questions SET votes = %s WHERE id = %s RETURNING *", (vote, id))
                downvoted_question = cur.fetchone()
                conn.commit()
                return downvoted_question
