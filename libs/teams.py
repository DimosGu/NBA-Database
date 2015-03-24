#!/usr/bin/env python

# Team options for the database #
import MySQLHelper
mysql_helper = MySQLHelper.MySQLHelper()

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
                edit_team()

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

    print("INSERT TEAM HERE")
    name = raw_input("\nEnter team name: ")
    gm = raw_input("Enter general manager: ")
    coach = raw_input("Enter coach: ")
    arena = raw_input("Enter arena: ")
    record = raw_input("Enter record: ")
    print("")

    test = 'INSERT INTO Team (arena, coach, general_manager, record, team_name) ' \
           'VALUES (%s, %s, %s, %s, %s)', (arena, coach, gm, record, name)
    mysql_helper.insert_data(test)

# Function for removing a team from the NBA
def remove_team():

    team = raw_input("\nEnter the team name you want to delete: ")
    test = "DELETE FROM Team WHERE team_name LIKE %s", ("%" + team + "%",)
    mysql_helper.insert_data(test)


# Function for editing the team
def edit_team():

    team = raw_input("\n Enter team name to change attribute for: ")
    print("Which of these attributes:")
    print("team_name, general_manager, coach, arena, record")
    which_att = raw_input("Would you like to change: ")
    change_att = raw_input("Change to: ")

    if which_att == "coach":
        test = 'UPDATE Team SET coach = %s WHERE team_name = %s', (change_att, team)
    elif which_att == "arena":
        test = 'UPDATE Team SET arena = %s WHERE team_name = %s', (change_att, team)
    elif which_att == "record":
        test = 'UPDATE Team SET record = %s WHERE team_name = %s', (change_att, team)
    elif which_att == "team_name":
        test = 'UPDATE Team SET team_name = %s WHERE team_name = %s', (change_att, team)
    elif which_att == "general_manager":
        test = 'UPDATE Team SET general_manager = %s WHERE team_name = %s', (change_att, team)
    else:
        print("You have entered a non-existing team name")
    mysql_helper.insert_data(test)