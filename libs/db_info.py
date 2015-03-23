#!/usr/bin/env python

# NBA Database Information

def showInformation(cursor):

    # Find the number of tables in the database
    number_rows = 'SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = "NBA"'
    cursor.execute(number_rows)

    for result in cursor:
        print("Database Tables: {0}".format(result[0]))

    # List all of the players and the data
    test = 'SELECT * FROM Player'
    cursor.execute(test)

    for testing in cursor:
        print("Testing: {0}".format(testing))