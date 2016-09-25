#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 06, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#
#

# Imports


# define a class object
class Human():
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
	
    def print_name(self):
        print("The name of the object is : \"%s\" " % self.name)
	
    
    def perform_math_task(self,math_operation, *args):
        print("%s performed math operation" % self)
	
	
	
# now, define a function outside of the class Human
def addnumbers(a,b):
    return a + b
    
bhishan = Human("Bhishan Poudel", "Male")

bhishan.print_name()
    
