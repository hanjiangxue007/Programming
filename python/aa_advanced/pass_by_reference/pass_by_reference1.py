#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 11, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. Exmaple of pass by reference.
#
#

class PassByReference:
    def __init__(self, name):
        self.name = name

def changeRef(ref):
    ref[0] = PassByReference('Michael')

# usage
obj = PassByReference('Peter')
print (obj.name) # Peter

# A pointer to obj! ;-)
p = [obj] 
changeRef(p)
print (p[0].name) # p->name  Michael
print (obj.name)  # Peter
