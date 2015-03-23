#!/usr/bin/env python

# Config File #
# Used for program settings and initialization #
import mysql.connector

MySQLConfig = {
  'user': '',
  'password': '',
  'host': '',
  'database': 'NBA',
  'raise_on_warnings': True,
}

# Initialize MySQL Connection + Cursor
cnx = mysql.connector.connect(**MySQLConfig)

def createCursor():
    return cnx.cursor()

# Example query with cursor
# query = 'SHOW tables'
# cursor.execute(query)
#
# for row in cursor:
#     print(row)
