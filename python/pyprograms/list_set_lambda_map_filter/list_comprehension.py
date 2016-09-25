#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

# Program   : list comprehension

numbers = [1,2,3,4,5]
doubled_odds = [n*2 for n in numbers if n%2 == 1]


# more readable
doubled_odds = [
    n*2
    for n in numbers
    if n%2 == 1
]

print(doubled_odds)



## using generator
#x = (x **2 for x in range(20))
#print(x) # generator object
## to use generator
#print(next(x))
#print(next(x))
#print(next(x))
#print(next(x))
#print(next(x))

## convert generator to list
#x = list(x)  # convert generator to a list
#print(x)

# double each elements
lst = [20, 24.5,36, 40]
lst2 = [ (x*2) for x in lst ]
print (lst2)

# temperature conversion
Celsius = [20, 24.5,36, 40]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print (Fahrenheit)


# square the element if it is integer
a_list = [1, '4', 9, 'a', 0, 5]
squared_ints = [ e**2 for e in a_list if type(e) == int ]
print (squared_ints)


# using filer and map
a_list = [1, '4', 9, 'a', 0, 5]
squared_ints = map(  lambda e: e**2, filter(lambda e: type(e) == int, a_list)    )
print (squared_ints)

