#!/usr/bin/python3
"""
4-cities_by_state.py
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


def print_cities(db):
    """prints all cities from input DB"""
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "INNER JOIN states ON states.id = cities.state_id "
                "ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    print_cities(init_db())
