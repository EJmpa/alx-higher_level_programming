#!/usr/bin/python3
"""
This script creates the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

# Check if the script is being executed as the main module
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

    # Create all tables defined in the Base class
    Base.metadata.create_all(engine)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create the State "California" and the City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    # Add the State and City objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
