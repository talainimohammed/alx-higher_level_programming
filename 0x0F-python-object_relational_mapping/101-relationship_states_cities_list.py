#!/usr/bin/python3
""" state models
"""
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    eng = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    objs = session.query(State).outerjoin(City).all()
    if objs:
        for state in objs:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")