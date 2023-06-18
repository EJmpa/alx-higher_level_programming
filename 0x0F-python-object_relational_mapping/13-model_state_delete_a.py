#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter "a"
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Checks if the script is being executed as the main module.
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

    # Query the State objects containing the letter "a"
    states = session.query(State).filter(State.name.like("%a%")).all()

    # Delete the State objects
    if states is not None:
        for state in states:
            session.delete(state)

    # Commit the session to persist the changes in the database
    session.commit()

    # Close the session
    session.close()
