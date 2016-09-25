#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016
# Ref     : https://www.python.org/dev/peps/pep-0238/
# Ref     : http://mazamascience.com/WorkingWithData/?p=587

# Imports
from __future__ import division # / is true division(gives decimal),
                                # // is floor divison

user_input = input("Enter the number to convert from celcius to  farenheit \
                    e.g. 18 or 18.0\n")
#user_input = 18.0
print(user_input * 9/5 + 32) # ans = 64.4


#user_input = 18
print(user_input * 9/5 + 32) # ans = 64.4 only for future


print(9//5)
