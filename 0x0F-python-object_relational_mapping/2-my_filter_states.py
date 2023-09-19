#!/usr/bin/python3
"""script for use in getting all states
"""
import MySQLdb
import sys


if __name__ == '__main__':
    query = "SELECT * FROM states WHERE name LIKE BINARY\
 '{}' ORDER BY id ASC".format(sys.argv[4])
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306
    )
    con = db.cursor()

    con.execute(query)
    rows = con.fetchall()

    for row in rows:
        print(row)

    con.close()
    db.close()
