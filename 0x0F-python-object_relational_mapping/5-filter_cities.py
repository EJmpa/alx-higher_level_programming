#!/usr/bin/python3
"""
This script  takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""
import sys
import MySQLdb

if len(sys.argv) != 5:
    print("Usage: python script.py [mysql_username] \
    [mysql_password] [database_name] [state_name]")
    sys.exit(1)

"""
Access to the database and get the states
from the database.
"""

if __name__ == '__main__':

    # Read MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all states from the states table
    query = "SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s \
    ORDER BY cities.id ASC"

    cursor.execute(query, (state_name,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the states
    if rows is not None:
        print(", ".join([row[1] for row in rows]))

    # Close the cursor and database connection
    cursor.close()
    db.close()
