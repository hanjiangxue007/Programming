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
import abc

class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the following properties:
    
    Attributes:
    name: A string representing the customer's name.
    balance: A float tracking the current balance of the customer's
             account.
    """
    
    def __init__(self,name,balance=0.0):
        """Return a Customer object whose name is *name* and 
        starting balance is *balance*.:
        """
        self.name = name
        self.balance = balance
        
    def withdraw(self,amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Error: Amount greater than available balance.')
        self.balance -= amount
        return self.balance
        
    def deposit(self,amount):
        """Return the balance remaining after depositting *amount*
        dollars."""
        self.balance += amount
        return self.balance
        

##================================================================
# create an instance of object Customer
bhishan = Customer('Bhishan Poudel', 1000.0)

# withdraw some money
bhishan.withdraw(100.0)

# withdraw again 
Customer.withdraw(bhishan,100.0)

# let's see,how much balance we have
print(bhishan.balance)

# deposit some money
bhishan.deposit(500.0)

# check balance
print(bhishan.balance)

        
    
    
    
    
