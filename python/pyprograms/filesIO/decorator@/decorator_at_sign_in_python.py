#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python



# =============================================================================
#This code snippet:

def decorator(func):
   return func

@decorator
def some_func():
    pass

#Is equivalent to this code:

def decorator(func):
    return func

def some_func():
    pass

some_func = decorator(some_func)

# In the definition of decorator you can add some modified things that
# wouldn't be returned by function normally
# =============================================================================



# example
# =============================================================================
class Pizza(object):
    def __init__(self):
        self.toppings = []
    def __call__(self, topping):
        # when using '@instance_of_pizza' before a function def
        # the function gets passed onto 'topping'
        self.toppings.append(topping())
    def __repr__(self):
        return str(self.toppings)

pizza = Pizza()

@pizza
def cheese():
    return 'cheese'
@pizza
def sauce():
    return 'sauce'

print pizza
# ['cheese', 'sauce']

# =============================================================================

