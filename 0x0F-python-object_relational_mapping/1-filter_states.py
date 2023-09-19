#!/usr/bin/python3
"""script that lists all states with a name starting with N
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306
    )
    con = db.cursor()

    con.execute("SELECT * FROM states WHERE name \
LIKE BINARY 'N%' ORDER BY id ASC")
    rows = con.fetchall()

    for row in rows:
        print(row)

    con.close()
    db.close()
