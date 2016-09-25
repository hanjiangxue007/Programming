#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 16, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. 
#
#

# Imports
import collections

# here's a dictionary we want to avoid dirty'ing
d = {i: i for i in range(10)}

# wrap into a chain map and make changes there
c = collections.ChainMap({}, d)

#Now we can dirty c without corresponding changes happening in d

c[0] = -100
print(c[0], d[0]) #  -100 0

# Whether this solution is appropriate depends on your use case ... 
# in particular the ChainMap will not behave like a regular map 
# when it comes to some things, like deleting keys:

del c[0]
print(c[0]) # 0

