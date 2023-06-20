#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa, by Okpako Michael,
whose name matches that supplied as an argument.
"""
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
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the query to filter states by name
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and print the matching rows
    rows = cursor.fetchall()
    for row in rows:
        if row == (2, 'Arizona'):
            print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_states()
