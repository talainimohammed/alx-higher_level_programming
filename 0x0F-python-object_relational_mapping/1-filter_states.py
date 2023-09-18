#!/usr/bin/python3
"""script that lists all states with a name starting with N
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    user = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=user,
                         passwd=password, db=data,
                         port=3306)
    cur = db.cursor()
    num_rows = cur.execute('''
            SELECT * FROM states
            WHERE states.name LIKE 'N%'
            ORDER BY states.id
            ''')
    rows = cur.fetchall()
    for row in rows:
        print(row)
