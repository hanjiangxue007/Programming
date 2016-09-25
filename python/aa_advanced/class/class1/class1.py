#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 17, 2016
# Last update : 
#

class Person():
    AnotherName = 'Bhishan Poudel'
    def __init__(self):
        self.FirstName = 'Paribartan'
        self.LastName = 'Poudel'

    def get_name(self):
        return self.FirstName + ' ' + self.LastName

class Employee(Person):
    def __init__(self):
        Person.__init__(self)  # don't forget this line
        self.empnum = "abc123"

    def get_emp(self):
        print(self.AnotherName)
        return self.FirstName + ' ' + 'abc'

x = Person()
y = Employee()
print(x.get_name())
print(y.get_emp())

