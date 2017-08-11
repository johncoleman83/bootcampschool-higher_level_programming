#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def init_sess():
    """initializes session and engine for sqlalchemy DB instance"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    return (engine, session)


def print_cities(db):
    """prints all the cities from session DB"""
    session = db[1]
    i = session.query(City, State).filter(State.id == City.state_id)
    for c, s in i:
        print(s.name, ': ({}) '.format(c.id), c.name, sep='')
    session.close()
    db[0].dispose()

if __name__ == '__main__':
    print_cities(init_sess())
