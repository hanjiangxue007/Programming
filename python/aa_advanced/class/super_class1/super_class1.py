#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 17, 2016
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

class Person(object):
    AnotherName = 'Bhishan Poudel'
    def __init__(self):
        super(Person, self).__init__()
        self.FirstName = 'Paribartan'
        self.LastName = 'Poudel'

    def get_name(self):
        return self.FirstName + ' ' + self.LastName

class Employee(Person):
    def __init__(self):
        super(Employee, self).__init__() # can access self.AnotherName
        self.empnum = 'abc123'

    def get_emp(self):
        print(self.AnotherName)
        return self.FirstName + ' ' + 'abc'

# usage
x = Person()
y = Employee()
print(x.get_name())
print("\n")
print(y.get_emp())
