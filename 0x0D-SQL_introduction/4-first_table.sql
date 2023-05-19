-- creates a table called first_table in the current database in my MySQL server.
-- first_table description:id INT, name VARCHAR(256)
-- If the table first_table already exists, my script should not fail
--#!/bin/bash

--# Get the database name as an argument
database="$1"

--# SQL query to create the table
query="CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);"

# Execute the SQL query using the mysql command
mysql -u username -p -e "$query" "$database"

