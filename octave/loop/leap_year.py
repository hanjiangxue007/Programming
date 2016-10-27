#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016
# Ref     : https://www.rosettacode.org/wiki/Leap_year#Python

# Function to print leap year
# function to print leap year
def print_leap_year(year,value):
    if value == True:
	print("The given year",year,"is leap year.")

    else:
	print("The given year",year,"is not a leap year.")

##=============================================================================
# method 1
import calendar
year = 2001
value = calendar.isleap(year)
print_leap_year(year,value)

##=============================================================================
# method 2
def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


year = 2016
value = is_leap_year(year)
print_leap_year(year,value)

##=============================================================================
# method 3
import datetime

def is_this_leap_year(year):
    try:
        datetime.date(year, 2, 29)  # second month has 29 days?
    except ValueError:
        return False
    return True

year = input("Enter the year: ")  # input for numbers, raw_input for strings
value = is_this_leap_year(year)
print_leap_year(year,value)
