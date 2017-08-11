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
    return (engine, session)


def add_state(db):
    """adds state to the DB"""
    session = db[1]
    s = State()
    s.name = "Louisiana"
    session.add(s)
    session.commit()
    r = session.query(State).filter(State.name == "Louisiana")
    print(r[0].id)
    session.close()
    db[0].dispose()


if __name__ == '__main__':
    add_state(init_sess())
