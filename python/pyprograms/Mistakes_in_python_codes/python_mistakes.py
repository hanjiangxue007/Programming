#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 08, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#
#

# Imports
import numpy as np



# same variables inside and outside a function
#someVar = 42

#def myFunction():
    #print(someVar)
    #someVar = 100

#myFunction()
 #UnboundLocalError: local variable 'someVar' referenced before assignment

# Using a local variable in a function that has the same name as a 
# global variable is tricky. The rule is: if a variable in a function 
# is ever assigned something, it is always a local variable when 
# used inside that function. Otherwise, it is the global variable 
# inside that function.


##===================================================================

## example 2
spam = ['cat', 'dog', 'mouse']
for i in range(len(spam)):  # forgetting len
    print(spam[i])

