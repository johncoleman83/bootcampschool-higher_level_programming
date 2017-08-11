#!/usr/bin/python3
"""
10-model_state_my_get.py
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker


def init_sess():
    """initializes session instance of DB using sqlalchemy"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    return (engine, session)


def parse_input(s):
    """parses input removing single quotes and semicolons"""
    REP_CHARS = [';', "'", '"']
    for i in REP_CHARS:
        s = s.replace(i, '--')
    return s


def print_state_name(db):
    """prints the ID of input state"""
    session = db[1]
    n = parse_input(sys.argv[4])
    r = session.query(State).filter(State.name == n)
    try:
        print(r[0].id)
    except:
        print("Not found")
    session.close()
    db[0].dispose()


if __name__ == '__main__':
    print_state_name(init_sess())
