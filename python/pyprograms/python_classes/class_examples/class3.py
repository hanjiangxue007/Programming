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

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

# instanciation
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

# using instance objects
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

##===================================================================
## We can add, remove, or modify attributes of classes and objects
emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del (emp1.age)  # Delete 'age' attribute.

# another way of using attributes
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
getattr(emp1, 'age')    # Returns value of 'age' attribute
delattr(emp1, 'age')    # Delete attribute 'age'

# built_in class attributes
print ("\nEmployee.__doc__:", Employee.__doc__)
print ("\nEmployee.__name__:", Employee.__name__)
print ("\nEmployee.__module__:", Employee.__module__)
print ("\nEmployee.__bases__:", Employee.__bases__)
print ("\nEmployee.__dict__:", Employee.__dict__ )
   
