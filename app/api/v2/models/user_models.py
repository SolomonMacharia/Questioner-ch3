from . import cur, conn

class Users:
    def __init__(self):
        pass

    def create_user(self, username, email, password, confirm_password):
        cur.execute('''INSERT INTO users(username, email, password, confirm_password) VALUES(%s, %s, %s, %s );''',\
         (username, email, password, confirm_password))
        conn.commit()

    