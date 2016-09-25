#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 11, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. logging examples
#
# 

#   CRITICAL – for very serious errors
#   ERROR – for less serious errors
#   WARNING – for warnings
#   INFO – for important informative messages
#   DEBUG – for detailed debugging messages


# Imports
import logging

# log messages to a file, ignoring anything less severe than ERROR
logging.basicConfig(filename='log.txt', level=logging.INFO)


# these messages should appear in our file
logging.error("The washing machine is leaking!")
logging.critical("The house is on fire!")

# but these ones won't
logging.warning("We're almost out of milk.")
logging.info("It's sunny today.")
logging.debug("I had eggs for breakfast.")

# try exception
try:
    age = int(input("How old are you? "))
except ValueError as err:
    logging.exception(err)




