#!/usr/bin/env python

# Search for specific things in the NBADatabase

import MySQLHelper
mysql_helper = MySQLHelper.MySQLHelper()
cursor = mysql_helper.cursor

teamList = ["Team ID", "Team name", "General Manager", "Coach", "Arena", "Record"]
playerList = ["Player ID", "Player name", "Draft Year"]
gameList = ["Game ID", "Referees", "Location", "Winner", "Score"]

def nba_search():

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

            # Search for a team by name
            if operation == 1:
                print("Search For A Team")
                team_name = raw_input("\nName To Search: ")

                team_query = 'SELECT * FROM Team WHERE team_name = %s', (team_name,)
                cursor.execute(*team_query)
                results = cursor.fetchall()

                print("Search Results")
                if results:
                    # Print out all the results if they exist
                    for x in results:
                        print(x)
                else:
                    print("No teams with that name were found!")

            # Search for a player by name
            elif operation == 2:
                print("Search For A Player")
                player_name = raw_input("\nName To Search: ")

                team_query = 'SELECT * FROM Player WHERE name = %s', (player_name,)
                cursor.execute(*team_query)
                results = cursor.fetchall()

                print("Search Results")
                if results:
                    # Print out all the results if they exist
                    for x in results:
                        print(x)
                else:
                    print("No players with that name were found!")

            # Search for a game by location
            elif operation == 3:
                print("Search For A Game")
                location = raw_input("\nLocation To Search: ")

                team_query = 'SELECT * FROM Game WHERE location = %s', (location,)
                cursor.execute(*team_query)
                results = cursor.fetchall()

                print("Search Results")
                if results:
                    # Print out all the results if they exist
                    for x in results:
                        print(x)
                else:
                    print("No games with that location were found!")

        print_menu()


def print_menu():

    print("")
    print("\t Search Options List:")
    print("\t 1 - Search For Team")
    print("\t 2 - Search For Player")
    print("\t 3 - Search For Game")
    print("\t 0 - Main Menu")
    print("")