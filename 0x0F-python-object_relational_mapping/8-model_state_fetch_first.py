#!/usr/bin/python3
"""
8-model_state_fetch_first.py
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


def print_min_state(db):
    """prints the state with min value using first()"""
    session = db[1]
    instance = session.query(State).first()
    try:
        print(instance.id, ': ', instance.name, sep='')
    except:
        print("Nothing")
    session.close()
    db[0].dispose()


if __name__ == '__main__':
    print_min_state(init_sess())
