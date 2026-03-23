#!/usr/bin/python3
"""script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    statesearch = sys.argv[4]

    Session = sessionmaker(bind=engine) # crée une fabrique de sessions
    session = Session() # ouvre la session (comme un curseur)

    state = session.query(State).filter(
        State.name == sys.argv[4]
    ).first()

    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))



    session.close()
