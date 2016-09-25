#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 26, 2016
# Last update : 
#
# Depends     : none
#
# Outputs     : 
#
# Info:
# 1. 
#

# Imports



import datetime

now = datetime.datetime.now()

print()
print("Current date and time using str method of datetime object:")
print(str(now))

print()
print("Current date and time using instance attributes:")
print("Current year: %d" % now.year)
print("Current month: %d" % now.month)
print("Current day: %d" % now.day)
print("Current hour: %d" % now.hour)
print("Current minute: %d" % now.minute)
print("Current second: %d" % now.second)
print("Current microsecond: %d" % now.microsecond)

print()
print("Current date and time using strftime:")
print(now.strftime("%Y-%m-%d %H:%M"))

print()
print("Current date and time using isoformat:")
print(now.isoformat())


print (datetime.date.today().strftime("%x"))