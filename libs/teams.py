#!/usr/bin/env python

# Team options for the database #
import MySQLHelper
mysql_helper = MySQLHelper.MySQLHelper()
cursor = mysql_helper.cursor

def team_options():
    print_menu()
    insert_team()


# Function for printing sub-menu
def print_menu():
    print("\t Team Options List:")
    print("\t 1 - Insert Team")
    print("\t 2 - Remove Team")
    print("\t 3 - Edit Team")


def insert_team():
    # print("INSERT TEAM HERE")
    # name = raw_input("\nEnter team name: ")
    # gm = raw_input("Enter general manager: ")
    # coach = raw_input("Enter coach: ")
    # arena = raw_input("Enter arena: ")
    # record = raw_input("Enter record: ")
    # print("")

    test = 'INSERT INTO Team (arena, coach, general_manager, record, team_name) ' \
           'VALUES ("Air Canada", "Dwyane Casey", "Masai Uiri", "33-1", "Raptor")'
    mysql_helper.insert_data(test)

'''
def removeTeam():
    #

def editTeam():
    #
'''