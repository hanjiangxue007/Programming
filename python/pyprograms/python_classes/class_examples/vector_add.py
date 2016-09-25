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
from __future__ import print_function
from __future__ import division
from operator import add,sub,mul,truediv


class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector ({0}, {1})'.format(self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
      
   def __sub__(self,other):
       return Vector(self.a - other.a, self.b - other.b)
       
   def __mul__(self,other):
       return Vector(self.a * other.a, self.b * other.b)
    
   # __div__ does not work when  __future__.division is used   
   def __truediv__(self, other):
       return Vector(self.a / other.a, self.b / other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
print (v1 - v2)
print (v1 * v2)
print (v1 / v2) # Vector(0,-5)

print(2/5) # 0.4
print(2//5) # 0
