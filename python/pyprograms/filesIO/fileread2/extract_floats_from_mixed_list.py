#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://stackoverflow.com/questions/14633703/in-python-how-to-convert-number-to-float-in-a-mixed-list


# Program   : extract floats from mixed list

a = ['str',5,'',4.1]

def convert(value):
    try:
        return float(value)
    except ValueError:
        return value

b = list(map(convert, a))
print(b)


# method 2
new_a = []
for x in a:
    try:
        new_a.append(float(x))
    except ValueError:
        new_a.append(x)

print(new_a)

# method 3
new_a = []
for x in a:
    try:
        new_a.append(float(x))
    except ValueError:
        pass

print(new_a)
