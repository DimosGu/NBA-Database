#!/usr/bin/env python

# Option to view the teams in database
import sys

def showTeams(cursor):

    attList = ["Team ID", "Team name", "General Manager", "Coach", "Arena", "Record"]
    x = 0
    # List all of the teams and the data
    test = 'SELECT * ' \
           ' FROM Team'

    cursor.execute(test)

    print

    for att in attList:
        print("{0:<20s} |".format(att)),

    print
    for testing in cursor:
        print("-"*136)
        for att in testing:
            print("{0:<20} |".format(att)),
        print

    print