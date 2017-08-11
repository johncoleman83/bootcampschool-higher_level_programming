#!/usr/bin/python3
"""
7-model_state_fetch_all.py
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def init_sess():
    """initializes session and engine for sqlalchemy DB instance"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    return (engine, session)


def print_states(db):
    """prints all the states from session DB"""
    session = db[1]
    for instance in session.query(State).order_by(State.id):
        print(instance.id, ': ', instance.name, sep='')
    session.close()
    db[0].dispose()

if __name__ == '__main__':
    print_states(init_sess())
