#!/usr/bin/env python

# MySQL Connect and Cursor Initialization #
# Used for providing structure and access to using MySQL #
import mysql.connector, config
config = config.get_config()


class MySQLHelper:

    def __init__(self):
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

    def commit_changes(self):
        self.cnx.commit()

    def close_connections(self):
        self.cursor.close()
        self.cnx.close()