#!/usr/bin/env python

# Option to view the players in database
import sys

def showPlayers(cursor):

    attList = ["Player ID", "Player name", "Draft Year"]
    # List all of the teams and the data
    test = 'SELECT * ' \
           ' FROM Player'

    cursor.execute(test)

    print

    for att in attList:
        print("{0:<20s} |".format(att)),

    print
    for testing in cursor:
        print("-"*67)
        for att in testing:
            print("{0:<20} |".format(att)),
        print

    print