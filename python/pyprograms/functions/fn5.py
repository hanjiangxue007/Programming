#!/usr/bin/env python
#author: bhishan poudel
#cmd   : clear; python fn5.py


from math import *  #importing every functions inside math
import math         # importing routine math


def cube(number):   # defining function cube
    return number*number*number

def myfunc(number): # defining function myfunc
    """
        The function 'myfunc' will take a number as an argument,
        it will return cube of the number if it divisilbe by 3
        otherwise, it will return the square of the number.
    """
    
    if (number % 3 == 0):
        number =  cube(number)
    else:
        number = number * number
    return number
    
print myfunc.__doc__  # printing the docstring of the function  
print "myfunc(3) = ", myfunc(3)
print "myfunc(4) = ", myfunc(4)


print
print "sqrt(25)      = ", sqrt(25)  # from math import sqrt or from math import * (everything)
print "math.sqrt(25) = ", (math.sqrt(25)) # import math
print

