#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa.
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

    # Query the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Check if the State object exists
    if state is not None:
        # Update the name of the State object
        state.name = "New Mexico"

        # Commit the session to persist the changes in the database
        session.commit()
    else:
        print("State not found")

    # Close the session
    session.close()
