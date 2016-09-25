#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 10, 2016
# Last update :
#
# Depends     : none
#
# Outputs     :
#


##==============================================================================
## Comparing things to None the wrong way
##==============================================================================
# anti pattern
number = None

if number == None:
    print("This works, but is not the preferred PEP 8 pattern")


# best practice
number = None

if number is None:
    print("PEP 8 Style Guide prefers this pattern")


##==============================================================================
##==============================================================================
# anti pattern
flag = True

# Not PEP 8's preferred pattern
if flag == True:
    print("This works, but is not the preferred PEP 8 pattern")

# best practice
flag = True

if flag:
    print("PEP 8 Style Guide prefers this pattern")

# WRONG
flag = True

if flag is True:
    print("PEP 8 Style Guide abhors this pattern")
