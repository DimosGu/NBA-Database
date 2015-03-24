#!/usr/bin/env python

# Option to view the teams in database
import MySQLHelper
mysql_helper = MySQLHelper.MySQLHelper()
cursor = mysql_helper.cursor


def show_teams():

    attList = ["Team ID", "Team Name", "General Manager", "Coach", "Arena", "Record"]
    # List all of the teams and the data
    test = 'SELECT * ' \
           ' FROM Team'

    cursor.execute(test)

    print("")

    for att in attList:
        print("{0:<20s} |".format(att)),

    print("")
    for testing in cursor:
        print("-"*136)
        for att in testing:
            print("{0:<20} |".format(att)),
        print("")

    print("")