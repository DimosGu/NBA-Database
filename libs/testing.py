#!/usr/bin/env python

# File for testing MySQL Queries
import mysql.connector

config = {
  'user': 'brandon',
  'password': 'brandon123',
  'host': 'personal.branchow.com',
  'database': 'NBA',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = 'INSERT INTO Team (arena, coach, general_manager, record, team_name) VALUES ("Air Canada", "Dwyane Casey", "Masai Uiri", "33-1", "Raptor")'
cursor.execute(query)

cnx.commit()
cnx.close()