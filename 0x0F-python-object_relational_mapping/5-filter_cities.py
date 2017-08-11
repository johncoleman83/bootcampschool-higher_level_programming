#!/usr/bin/python3
"""
5-filter_cities.py
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


def print_cities_by_state(db):
    """prints all cities from input DB"""
    cur = db.cursor()
    name = parse_input(sys.argv[4])
    cur.execute("SELECT cities.name FROM cities "
                "INNER JOIN states ON states.id = cities.state_id "
                "WHERE states.name LIKE BINARY '%{}%' "
                "ORDER BY cities.id ASC".format(name))
    print(', '.join([row[0] for row in cur.fetchall()]))
    cur.close()
    db.close()


if __name__ == "__main__":
    print_cities_by_state(init_db())
