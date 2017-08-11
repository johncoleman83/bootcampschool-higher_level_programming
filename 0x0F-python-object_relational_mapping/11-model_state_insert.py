#!/usr/bin/python3
"""
11-model_state_insert.py
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
    return session


def parse_input(s):
    """parses input removing single quotes and semicolons"""
    REP_CHARS = [';', "'", '"']
    for i in REP_CHARS:
        s = s.replace(i, '--')
    return s


def add_state(session):
    """adds state to the DB"""
    s = State()
    s.name = "Louisiana"
    session.add(s)
    session.commit()
    r = session.query(State).filter(State.name == "Louisiana")
    print(r[0].id)


if __name__ == '__main__':
    add_state(init_sess())
