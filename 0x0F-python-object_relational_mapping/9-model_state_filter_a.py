#!/usr/bin/python3
"""
Script that lists all State objects containing the letter "a"
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, database),
        pool_pre_ping=True
    )

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects containing the letter "a"
    states = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .order_by(State.id).all()
    )

    # Print the results
    for state in states:
        print("{0}: {1}".format(state.id, state.name))

    # Close the session
    session.close()
