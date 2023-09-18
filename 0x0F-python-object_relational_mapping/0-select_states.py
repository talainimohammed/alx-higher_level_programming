#!/usr/bin/python3
"""Lists all states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    con.close()
