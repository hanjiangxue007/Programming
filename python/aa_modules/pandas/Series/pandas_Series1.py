#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/

# Imports
import numpy as np
import pandas as pd


# create a Series with an arbitrary list
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
print(s)
print("\n")


# Alternatively, you can specify an index to use when creating the Series.
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
              index=['BH', 'I', 'SH', 'A', 'N'])
print(s)
print("\n")

# The Series constructor can convert a dictonary as well,
# using the keys of the dictionary as its index.
d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
print(cities)
print("\n")

# You can use the index to select specific items from the Series ...
print(cities['Chicago'])
a = cities[['Chicago', 'Portland', 'San Francisco']]
print(a)
print("\n")

# Or you can use boolean indexing for selection.
a = cities[cities < 1000]
print(a)
print("\n")

# use boolean
print('{} {} {} {}'.format('\nuse of boolean: ', '','','\n'))
less_than_1000 = cities < 1000
print(less_than_1000)
print('\n')
print(cities[less_than_1000])

# changing based on the index
print('{} {} {} {}'.format('\nchanging based on the index', '','',''))
print('Old value:', cities['Chicago'])
cities['Chicago'] = 1400
print('New value:', cities['Chicago'])

# changing values using boolean logic
print('{} {} {} {}'.format('\nchanging values using boolean logic = ', '','',''))
print(cities[cities < 1000])
print('\n')
cities[cities < 1000] = 750
print cities[cities < 1000]


# What if you aren't sure whether an item is in the Series?
# You can check using idiomatic Python.
print('Seattle' in cities)
print('San Francisco' in cities)

# Mathematical operations can be done using scalars and functions.
# divide city values by 3
print("\nMathematical operations")
a = cities / 3
print(a)
print("\n")


# square city values
print('{} {} {} {}'.format('\nsquare city values ', '','',''))
a = np.square(cities)
print(a)
print("\n")

# You can add two Series together, which returns a union of the two Series
# with the addition occurring on the shared index values. Values on either
# Series that did not have a shared index will produce a NULL/NaN (not a number).
print('{} {} {} {}'.format('\nAdd two series', '','',''))
print(cities[['Chicago', 'New York', 'Portland']])
print('\n')
print(cities[['Austin', 'New York']])
print('\n')
print(cities[['Chicago', 'New York', 'Portland']] + cities[['Austin', 'New York']])


# Notice that because Austin, Chicago, and Portland were not found in
# both Series, they were returned with NULL/NaN values.
# NULL checking can be performed with isnull and notnull.

# returns a boolean series indicating which values aren't NULL
print('{} {} {} {}'.format('\nNULL checking ', '','',''))
a = cities.notnull()
print(a)
print("\n")

# use boolean logic to grab the NULL cities
print('{}'.format('\nuse boolean logic to grab the NULL cities',))
print(cities.isnull())
print('\n')
print(cities[cities.isnull()])



