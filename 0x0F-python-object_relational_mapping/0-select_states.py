#!/usr/bin/python3
"""
0-select_states.py
"""
import MySQLdb
import sys

HOST = 'localhost'
PORT = 3306
UN = sys.argv[1]
PW = sys.argv[2]
DBNM = sys.argv[3]


def print_states():
    """
    function prints all states from input DB
    """
    db = MySQLdb.connect(host=HOST,
                         port=PORT,
                         user=UN,
                         passwd=PW,
                         db=DBNM)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    print_states()
