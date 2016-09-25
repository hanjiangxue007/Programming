#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 07, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#
#

# Imports
import abc

# define parent class
class Parent:        
   def myMethod(self):
      print ('Calling parent method')

# define child class
class Child(Parent): 
   def myMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method
p = Parent()         # instance of parent
p.myMethod()         # parent method


