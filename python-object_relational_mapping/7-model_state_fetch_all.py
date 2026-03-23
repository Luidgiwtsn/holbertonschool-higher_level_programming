#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    

    Session = sessionmaker(bind=engine) # crée une fabrique de sessions
    session = Session() # ouvre la session (comme un curseur)

    states = session.query(State).order_by(State.id).all() # SELECT * FROM states ORDER BY id ASC fetchall() → retourne une liste d'objets State

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
