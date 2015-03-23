#!/usr/bin/env python

# NBA Database Information

def showInformation(cursor):

    # MySQL Version
    version = 'SELECT VERSION()'
    cursor.execute(version)
    print("MySQL Server Version: {0}".format(cursor.fetchone()[0]))

    # Find the number of tables in the database
    number_rows = 'SELECT COUNT(*)' \
                  'FROM information_schema.tables ' \
                  'WHERE table_schema = "NBA"'
    cursor.execute(number_rows)
    print("Total Tables: {0}".format(cursor.fetchone()[0]))

    # Get total number of records in the database
    total_records = 'SELECT SUM(TABLE_ROWS) ' \
                    'FROM INFORMATION_SCHEMA.TABLES ' \
                    'WHERE TABLE_SCHEMA = "NBA"'
    cursor.execute(total_records)
    print("Total Entries: {0}".format(cursor.fetchone()[0]))

    # Line Spacing
    print("")

    # for testing in cursor:
    #     print("Testing: {0}".format(testing))