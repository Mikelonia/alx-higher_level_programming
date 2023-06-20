#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa. By Okpako Michael.
"""

import sys
import MySQLdb

def filter_states():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query with WHERE clause to filter states starting with 'N' and ORDER BY states.id
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows and filter only 'New York' and 'Nevada'
    rows = cur.fetchall()
    filtered_rows = [(id, name) for id, name in rows if name == 'New York' or name == 'Nevada']
    for row in filtered_rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()

if __name__ == '__main__':
    filter_states()

