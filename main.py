#!/usr/bin/env python

# CP363 Final Assignment #
# NBA Database #
# Brandon Chow - 129006542 and Tudor Bertian - 130318270 #

# Import necessary libraries
import config
from libs import menu, db_info

cursor = config.createCursor()

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
            db_info.showInformation(cursor)
        elif operation ==2:
            print("Operaton 2")
        elif operation ==3:
            print("Operaton 3")
        elif operation ==4:
            print("Operaton 4")
        elif operation ==5:
            print("Operaton 5")
        elif operation ==6:
            print("Operaton 6")
        elif operation ==7:
            print("Operaton 7")

        menu.printMenu()