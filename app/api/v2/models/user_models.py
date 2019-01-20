from migrate import db_connection
conn = db_connection
cur = conn.cursor()


class Users:
    def __init__(self):
        self.db = db_connection

    def create_user(self, username, email, password, confirm_password):
        cur.execute('''INSERT INTO users(username, email, password, confirm_password) VALUES(%s, %s, %s, %s );''',\
         (username, email, password, confirm_password))
        conn.commit()

    