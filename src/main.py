from util.db import PGDatabase


if __name__ == '__main__':
    db = PGDatabase().db

    cur = db.cursor()

    cur.execute('SELECT * FROM test')
    print(cur.fetchall())


