#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016
# Ref     : https://pyformat.info/

# Imports
from __future__ import division
from __future__ import print_function


# Basic formatting
print("Basic formatting\n")
print('{} {}'.format(1, 2))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

# Padding and aligning strings
print("\nPadding and aligning strings")
print('{:10}'.format('test')) # align left
print('{:>10}'.format('test')) # align right
print('{:^10}'.format('test')) # align center

print("\n")
print('{:<{}s}'.format('test', 8)) # align left with argument
print('{:_<10}'.format('test')) # padding with _


# Truncating long strings
print("\nTruncating long strings")
print('{:.5}'.format('xylophone'))
print('{:.{}}'.format('xylophone', 7)) # truncate using argument

# Combining truncating and padding
print("\nCombining truncating and padding")
print('{:10.5}'.format('xylophone'))

# numbers
print("\nnumbers")
print('{:d}'.format(42))
print('{:f}'.format(3.141592653589793))
import math
print('{:f}'.format(math.pi))


# padding numbers
print("\npadding numbers")
print('{:4d}'.format(42))
print('{:06.2f}'.format(3.141592653589793))
print('{:04d}'.format(42))

# Signed numbers
print("\nSigned numbers")
print('{:+d}'.format(42))
print('{: d}'.format((- 23)))
print('{: d}'.format(42))
print('{:=5d}'.format((- 23)))

# Named placeholders
print("\nNamed placeholders")
data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data))
print('{first} {last}'.format(first='Hodor', last='Hodor!')) # keyword arguments


# Getitem and Getattr
print("\nGetitem and Getattr")
person = {'first': 'Bhishan', 'last': 'Poudel'} # setup
print('{p[first]} {p[last]}'.format(p=person))

data = [4, 8, 15, 16, 23, 42]
print('{d[4]} {d[5]}'.format(d=data))

# As well as accessing attributes on objects via getattr():
#This operation is not available with old-style formatting.

class Plant(object):
    type = 'tree'
print('{p.type}'.format(p=Plant()))

class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]
print('{p.type}: {p.kinds[0][name]}'.format(p=Plant()))


# Datetime
print("\nDatetime")
from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))

# Custom objects
print("\nCustom objects")
class my_class(object):

    def __format__(self, format):
        if (format == 'myformat'):
            return "I'm afraid I can't do that."
        return 'my_class'
print('{:myformat}'.format(my_class()))
print('{:hello}'.format(my_class()))
