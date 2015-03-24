#!/usr/bin/env python

# Config File #
# Used for program settings and initialization #

# MySQL Database Settings
def get_config():
    config =  { 'user': 'brandon',
                'password': 'brandon123',
                'host': 'personal.branchow.com',
                'database': 'NBA',
                'raise_on_warnings': True}
    return config