#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 06, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1. Example of Abstract Base Classes (ABC).
#
#

# Imports
from abc import ABCMeta, abstractmethod

class Vehicle(object):
    """A vehicle for sale by Bhishanco Car Dealership.
    
    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """
    
    __metaclass__ = ABCMeta
    
    base_sale_price = 0
    
    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""        
        if self.solf_on is not None:
            return 0.0 # Already sold
        return 5000.0 * self.wheels
        
    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""        
        if self.sold_on is None:
            return 0.0 # Not yet sold
        return self.base_sale_price - (.10 * self.miles)
        
    @abstractmethod
    def vehicle_type():
        """"Return a string representing the type of vehicle this is."""
        pass 
        
##=============================================================================
# Now, define Car and Truck classes

class Car(Vehicle):
    """A car for sale by Jeffco Car Dealership."""
    
    base_sale_price = 8000
    wheels = 4
    
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'
        
class Truck(Vehicle):
    """A truck for sale by Jeffco Car Dealership."""
    
    base_sale_price = 10000
    wheels = 4
    
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'
        
class Motorcycle(Vehicle):
    """A motorcycle for sale by Jeffco Car Dealership."""

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'motorcycle'
        

