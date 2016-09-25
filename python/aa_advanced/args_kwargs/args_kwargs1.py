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
# 1. Example of *args and **kwargs
# args = arguments
# kwargs = keyword arguments
#

def func(required_arg, *args, **kwargs):
    # required_arg is a positional-only parameter.
    print (required_arg)

    # args is a tuple of positional arguments,
    # because the parameter name has * prepended.
    if args: # If args is not empty.
        print (args)

    # kwargs is a dictionary of keyword arguments,
    # because the parameter name has ** prepended.
    if kwargs: # If kwargs is not empty.
        print (kwargs)

#func()
#Traceback (most recent call last):
  #File "<stdin>", line 1, in <module>
#TypeError: func() takes at least 1 argument (0 given)

print('{} {} {}'.format('\nexample 2','', ''))
func("required argument")
#required argument

print('{} {} {}'.format('\nexample 3','', ''))
func("required argument", 1, 2, '3')
#required argument
#(1, 2, '3')

print('{} {} {}'.format('\nexample 4','', ''))
func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")
#required argument
#(1, 2, '3')
#{'keyword2': 'foo', 'keyword1': 4}
