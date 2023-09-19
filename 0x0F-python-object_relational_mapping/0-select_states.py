#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db_host = "localhost"
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    con = db.cursor()

    con.execute("SELECT * FROM states ORDER BY id ASC")
    rows = con.fetchall()

    for row in rows:
        print(row)

    con.close()
    db.close()
    
