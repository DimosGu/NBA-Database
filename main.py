#!/usr/bin/env python

# CP363 Final Assignment #
# NBA Database #
# Brandon Chow - 129006542 and Tudor Bertiean - 130318270 #

# Import necessary libraries
from libs import menu, db_info, view_team, view_player, teams

indicator = True
inputs = [1, 2, 3, 4, 5, 6, 7]

# Start menu for operations
print("Welcome to the NBADatabase \n")
menu.printMenu()

# While loop for menu and getting user input
while indicator:

    operation = input("\nSelect an operation: ")

    if operation == 0:
        print(" \n Program Exiting! \n")
        indicator = False
        break

    else:
        if operation not in inputs:
            print("\n Invalid Operation! \n")

        # Flow for operations in the program
        if operation == 1:
            db_info.show_information()
        elif operation == 2:
            view_team.showTeams(cursor)
        elif operation == 3:
            view_player.showPlayers(cursor)
        elif operation == 4:
            print("Operation 4")
        elif operation == 5:
            print("Operation 5")
        elif operation == 6:
            print("Operation 6")
        elif operation == 7:
            print("Operation 7")

        menu.printMenu()