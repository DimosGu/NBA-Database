#!/usr/bin/env python

# Player options for the database #
import MySQLHelper

def player_options():

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
                print("Inserting Player...")
                insert_team()
            elif operation == 2:
                print("Removing Player...")
                remove_player()
            elif operation == 3:
                print("Editing Player...")

        print_menu()

# Function for printing sub-menu
def print_menu():

    print("")
    print("\t Player Options List:")
    print("\t 1 - Insert Player")
    print("\t 2 - Remove Player")
    print("\t 3 - Edit Player")
    print("\t 0 - Main Menu")
    print("")


def insert_team():
    mysql_helper = MySQLHelper.MySQLHelper()
    cursor = mysql_helper.cursor

    print("INSERT Player HERE")
    name = raw_input("\nEnter player name: ")
    draft_year = raw_input("Enter draft year: ")
    print("")

    test = 'INSERT INTO Player (draft_year, name) ' \
           'VALUES (%s, %s)', (draft_year, name)

    mysql_helper.insert_data(test)

def remove_player():
    mysql_helper = MySQLHelper.MySQLHelper()
    cursor = mysql_helper.cursor

    name = raw_input("\nEnter the player name you want to delete: ")
    test = "DELETE FROM Player WHERE name LIKE %s", ("%" + name + "%",)
    mysql_helper.insert_data(test)