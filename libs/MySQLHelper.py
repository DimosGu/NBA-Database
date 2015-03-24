#!/usr/bin/env python

# MySQL Connect and Cursor Initialization #
# Used for providing structure and access to MySQL Database Server #
import mysql.connector, config
config = config.get_config()


class MySQLHelper:

    def __init__(self):
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

    def insert_data(self, query):
        self.cursor.execute(query)
        self.cnx.commit()
        self.cnx.close()