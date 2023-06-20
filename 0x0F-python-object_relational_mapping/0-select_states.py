#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
# by Okpako Michael
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query with LIMIT 5 and ORDER BY states.id
    cur.execute("SELECT * FROM states ORDER BY states.id ASC LIMIT 5")

    # Fetch all the rows and print them
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()

