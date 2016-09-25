#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 06, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1. static methods example
#
#


# example 1
class Car(object):
    
    wheels = 4
    
    def __init__(self,make,model):
        self.make = make 
        self.model = model 
        
mustang = Car('Ford', 'Mustang')
print(mustang.wheels)
    
    
# example 2
class Vehicle(object):
    
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels ==2
        
