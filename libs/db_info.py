#!/usr/bin/env python

# NBA Database Information
# Shows the general information of the database

import MySQLHelper
mysql_helper = MySQLHelper.MySQLHelper()
cursor = mysql_helper.cursor


def show_information():

    # MySQL Version
    version = 'SELECT VERSION()'
    cursor.execute(version)
    print("MySQL Server Version: {0:>7}".format(cursor.fetchone()[0]))

    # Find the number of tables in the database
    number_rows = 'SELECT COUNT(*)' \
                  'FROM information_schema.tables ' \
                  'WHERE table_schema = "NBA"'
    cursor.execute(number_rows)
    print("Total Tables: {0:>10}".format(cursor.fetchone()[0]))

    # Get total number of records / rows in the database
    total_records = 'SELECT SUM(TABLE_ROWS) ' \
                    'FROM INFORMATION_SCHEMA.TABLES ' \
                    'WHERE TABLE_SCHEMA = "NBA"'
    cursor.execute(total_records)
    print("Total Entries: {0:>10}".format(cursor.fetchone()[0]))

    # Total number of teams
    team_counter = 0
    team_records = 'SELECT * FROM Team'
    cursor.execute(team_records)
    for teams in cursor:
        team_counter += 1
    print("Total Teams: {0:>11}".format(team_counter))

    # Total number of players
    player_counter = 0
    player_records = 'SELECT * FROM Team'
    cursor.execute(player_records)
    for players in cursor:
        player_counter += 1
    print("Total Teams: {0:>11}".format(player_counter))

    # Line Spacing
    print("")

    # for testing in cursor:
    #     print("Testing: {0}".format(testing))