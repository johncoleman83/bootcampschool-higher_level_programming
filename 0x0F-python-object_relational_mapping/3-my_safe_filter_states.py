#!/usr/bin/python3
"""
3-my_safe_filter_states.py
"""
import MySQLdb
import sys


def init_db():
    """initializes a db with MySQLdb"""
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    return db


def parse_input(s):
    """parses input removing single quotes and semicolons"""
    s = ''.join([i for i in s if i != "'" and i != ';'])
    return s


def print_one_state(db):
    """prints one state from input DB with SQL injection safeguard"""
    cur = db.cursor()
    name = parse_input(sys.argv[4])
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY '%{}%' "
                "ORDER BY states.id ASC".format(name))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    print_one_state(init_db())
