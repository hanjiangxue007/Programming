#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 28, 2016


try:
  a = int(input("Enter 'a' "))
except ValueError:
  print('PLease input a valid integer')

print(a) # a = 3  success, a = a , we get NameError
