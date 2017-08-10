#!/usr/bin/python3
"""
0-select_states.py
"""
import MySQLdb
import sys

HOST = 'localhost:3306'
UN = sys.argv[1]
PW = sys.argv[2]
DBNM = sys.argv[3]
if __name__ == "__main__":
    db = MySQLdb.connect(host=HOST, user=UN, passwd=PW, db=DBNM)
    cur = db.cursor()
    cur.execute("SHOW * FROM states ORDER BY states.id ASC")
    cur.close()
    db.close()
