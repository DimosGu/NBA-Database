#!/usr/bin/env python

# Add a game to the database with statistics

import MySQLHelper
mysql_helper = MySQLHelper.MySQLHelper()
cursor = mysql_helper.cursor

def add_game():
    name = raw_input("\nEnter team name: ")
    gm = raw_input("Enter general manager: ")
    coach = raw_input("Enter coach: ")
    arena = raw_input("Enter arena: ")
    record = raw_input("Enter record: ")