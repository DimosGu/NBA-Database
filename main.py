#!/usr/bin/env python

# CP363 Final Assignment #
# NBA Database #
# Brandon Chow - 129006542 and Tudor Bertian - 130318270 #

# Import necessary libraries
import config

cursor = config.createCursor()

indicator = True
inputs = ["1", "2", "3", "4", "5", "6", "7"]

# Start menu for operations
print("Welcome to the NBADatabase")
print("\t 1 - NBADatabase Information")
print("\t 2 - View Teams")
print("\t 3 - View Players")
print("\t 4 - Team Options")
print("\t 5 - Player Options")
print("\t 6 - Season Options")
print("\t 7 - Search Options")
print("\t 0 - Exit Program")

# While loop for menu and getting user input
while indicator:

    operation = input("Select an operation: ")

    if operation == "0":
        print(" \n Program Exiting!")
        indicator = False
    else:
        for check in inputs:
            if check != operation:
                print(" \n Invalid Input! \n")
                break

        print("\t 1 - NBADatabase Information")
        print("\t 2 - View Teams")
        print("\t 3 - View Players")
        print("\t 4 - Team Options")
        print("\t 5 - Player Options")
        print("\t 6 - Season Options")
        print("\t 7 - Search Options")
        print("\t 0 - Exit Program")