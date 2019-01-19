from migrate import connect_db(url)

conn = connect_db(url)
cur = conn.cursor


class QuestionModels(object):
    pass
