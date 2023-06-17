#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""
import sys
import MySQLdb

"""
Access to the database and get the states
from the database.
"""

if __name__ == '__main__':

    # Read MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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
    query = "SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")

    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the states
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
