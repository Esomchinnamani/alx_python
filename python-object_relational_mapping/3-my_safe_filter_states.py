#!/usr/bin/python3

import MySQLdb
import sys

"""
Script that connects via MySQLdb
avoids SQL injection
"""

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("""Usage: Enter username:{}
              password:{}
              db_name:{}
              state_name:{}""".format(
            sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        port=3306,
        db=database
    )

    query = """SELECT * FROM states
               WHERE name LIKE BINARY %s
               ORDER BY id ASC"""

    cursor = db.cursor()
    cursor.execute(query, (state_name + '%',))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()