#!/usr/bin/env python

# MySQL File For Initialization, Connection and Settings
import mysql.connector

class MySQLConnector:

    def __init__(self):
        MySQLConfig = {'user': 'user','password': 'password','host': 'localhost','database': 'DB','raise_on_warnings': True}
        self.cnx = mysql.connector.connect(**MySQLConfig)
        self.cursor = self.cnx.cursor()

    def query(self,query):
        self.cursor.execute(query)