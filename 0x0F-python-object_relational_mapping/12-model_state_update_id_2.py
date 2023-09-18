#!/usr/bin/python3
"""script to list all state objects using sqlalchemy
"""
from model_state import Base, State

from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

import sys


if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # create custom session object class from database eng
    Session = sessionmaker(bind=eng)
    # create instance of new custom session class
    session = Session()
    new_state = session.query(State).filter(State.id == 2).one()
    new_state.name = 'New Mexico'
    session.commit()
