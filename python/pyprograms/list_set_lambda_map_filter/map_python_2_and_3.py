#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://stackoverflow.com/questions/1247486/python-list-comprehension-vs-map

# python map_python_2_and_3.py
# python3 map_python_2_and_3.py

# imports
import itertools


def square(x):
    return x*x

squares = map(square, [1, 2, 3])
print(list(squares)) # [1, 4, 9] for both
print(list(squares)) # [] for python3


# note: map can be lazy interable in python2 by itertoo.imap
print("\n\n")
squares = itertools.imap(square, [1, 2, 3])
print(list(squares)) # [1, 4, 9] for both
print(list(squares)) # [] for python3


