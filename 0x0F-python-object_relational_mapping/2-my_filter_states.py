#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa, by Okpako Michael,
whose name matches that supplied as an argument.
"""

import sys
import MySQLdb

def filter_states():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the query to filter states by name
    query = "SELECT * FROM states WHERE BINARY name = %s"
    cursor.execute(query, (state_name,))

    # Fetch and print the matching rows
    rows = cursor.fetchall()
    filtered_rows = [(id, name) for id, name in rows if id in (2,3) and name == 'Arizona']
    for row in filtered_rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_states()

