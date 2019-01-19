from migrate import connect_db(url)

conn = connect_db(url)
cur = conn.cursor


class Users:
    def __init__(self):
        self.db = connect_db(url)

    def create_user(self, username, email, password, confirm_password):
        query = '''INSERT INTO users(username, email, password, confirnPassword)\
          VALUES(%(username)s, %(email)s, %(passord)s, %(confirmPassord)s)'''
        cur.execute(query,)
        conn.commit()

    def get_all(self):
        cur.execute('''SELECT * FROM users''')
        data = cur.fetchall()

    def get_user(self, user_id):
        query = '''SELECT * FROM users WHERE user_id = user_id'''
        cur.execute(query,)
        data = cur.fetchone()

    def update_user(self, user_id):
        query = '''UPDATE users SET({},{},{},{}) WHERE user_id = user_id'''.format(username,
                                                                                   email, password, confirm_password)
        cur.execute(query,)

    def delete_user(self, user_id):
        cur.execute(
            '''DELETE FROM users WHERE user_id = %(user_id)s''', (user_id,))
        conn.commit()
        cur.close()
