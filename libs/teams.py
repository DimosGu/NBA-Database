#!/usr/bin/env python

# Team options for the database #
import MySQLHelper
mysql_helper = MySQLHelper.MySQLHelper()
cursor = mysql_helper.cursor

def team_options():

    print_menu()
    indicator = True
    inputs = [1, 2, 3]

    while indicator:
        operation = input("\nSelect an operation: ")

        if operation == 0:
            print("Returning to Main Menu...")
            break
        else:
            if operation not in inputs:
                print("\nInvalid Operation! \n")
            if operation == 1:
                print("Inserting Team...")
                insert_team()
            elif operation == 2:
                print("Removing Team...")
                remove_team()
            elif operation == 3:
                print("Editing Team...")

        print_menu()

# Function for printing sub-menu
def print_menu():

    print("")
    print("\t Team Options List:")
    print("\t 1 - Insert Team")
    print("\t 2 - Remove Team")
    print("\t 3 - Edit Team")
    print("\t 0 - Main Menu")
    print("")


def insert_team():
    print("Enter Team Details:")
    name = raw_input("\nEnter team name: ")
    gm = raw_input("Enter general manager: ")
    coach = raw_input("Enter coach: ")
    arena = raw_input("Enter arena: ")
    record = raw_input("Enter record: ")
    print("")

    test = 'INSERT INTO Team (arena, coach, general_manager, record, team_name) ' \
           'VALUES (%s, %s, %s, %s, %s)', (arena, coach, gm, record, name)

    mysql_helper.insert_data(test)

def remove_team():
    team = raw_input("\nEnter the team name you want to delete: ")
    test = "DELETE FROM Team WHERE team_name = '%s'", team

    mysql_helper.insert_data(test)