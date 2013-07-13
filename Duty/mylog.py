#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
My log file:
It saves in log files and display them to console

Thanks to http://sametmax.com/ecrire-des-logs-en-python/
"""


import logging


# Create the log object
logger = logging.getLogger()
# Set the level to DEBUG
logger.setLevel(logging.DEBUG)

# Create a design for log format
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# Create a file handler
steam_handler = logging.StreamHandler()
# Set the level to DEBUG
steam_handler.setLevel(logging.DEBUG)
# Append to logger object
logger.addHandler(steam_handler)
