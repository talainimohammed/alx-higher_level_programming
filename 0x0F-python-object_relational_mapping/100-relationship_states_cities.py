#!/usr/bin/python3
"""List all states 100"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    Sess = Session()
    new_state = State(name="California")
    Sess.add(new_state)
    Sess.commit()
    new_city = City(name="San Francisco", state_id=new_state.id)
    Sess.add(new_city)
    Sess.commit()
    Sess.close()