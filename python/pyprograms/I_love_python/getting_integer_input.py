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

i = 1
while True:
    myint = input("How many times do you want to repeat the sequence?  ")
    try:
        myint = int(myint)
        break
    except ValueError:
        print("Please enter an integer value... ")
        pass

while i <= myint:
    i += 1
    print(i)
  
#Python glossary for try-except blocks
#EAFP
    #Easier to ask for forgiveness than permission. 
    #This common Python coding style assumes the existence of valid keys 
    #or attributes and catches exceptions if the assumption proves false. 
    #This clean and fast style is characterized by the presence of many 
    #try and except statements. The technique contrasts with the LBYL style 
    #common to many other languages such as C.
    
##======================================================================
# I want to check that a value is a number. Let's say I don't care what sort
# of number -- float, int, complex, Fraction, Decimal, something else -- just
# that it is a number. Should I:>> Look Before I Leap:  
# Example of LYBL (Look Before I Leap)

print('{} {} {}'.format('\nexample 2\n','', ''))
from numbers import Number

x = 5
if isinstance(x, Number):
    print(x)
    
else:
    raise TypeError
