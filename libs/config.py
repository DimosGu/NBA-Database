#!/usr/bin/env python

# Config File #
# Used for program settings and initialization #

# MySQL Database Settings
def get_config():
    config =  { 'user': '',
                'password': '',
                'host': '',
                'database': 'NBA',
                'raise_on_warnings': True}
    return config