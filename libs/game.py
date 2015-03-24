#!/usr/bin/env python

# Add a game for a specific player into the database with statistics

import MySQLHelper
mysql_helper = MySQLHelper.MySQLHelper()
cursor = mysql_helper.cursor

def add_game():
    player_id = raw_input("\nEnter Player ID: ")
    game_id = raw_input("Enter Game ID: ")
    fgp = raw_input("Field Goal Percentages: ")
    turnovers = raw_input("Turnovers: ")
    steals = raw_input("Steals: ")
    rebounds = raw_input("Rebounds: ")
    assists = raw_input("Assists: ")
    points = raw_input("Points: ")

    # Insert statement into the database
    game_query = 'INSERT INTO Team (player_id, game_id, field_goal_percentage, turnovers, steals, rebounds, assists, points) ' \
                 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', \
                 (player_id, game_id, fgp, turnovers, steals, rebounds, assists, points)
    mysql_helper.insert_data(game_query)
    print("Game Has Been Inputted!")