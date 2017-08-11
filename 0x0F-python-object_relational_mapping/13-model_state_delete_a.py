#!/usr/bin/python3
"""
13-model_state_delete_a.py
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


def delete_a_states(db):
    """deletes all states with 'a' in the name"""
    session = db[1]
    instances = session.query(State).filter(State.name.like('%a%'))
    for instance in instances:
        session.delete(instance)
    session.commit()
    session.close()
    db[0].dispose()


if __name__ == '__main__':
    delete_a_states(init_sess())
