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

a = datetime.datetime.now().strftime("%m%d%H%M%S%f")

print(a)
print(type(a))

# %U = week no. of current week
# m = month
# f = microseconds
