#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 10, 2016
# Last update :
#
# Depends     : none
#
# Outputs     :
#
# Info:
# 1. http://docs.quantifiedcode.com/python-anti-patterns/readability/using_camelcase_in_fund%20=%20%7B%22first_name%22:%20%22Alfred%22,%20%22last_name%22:%22Hitchcock%22%7D%20for%20key,val%20in%20d.items():%20print(%22%7B%7D%20=%20%7B%7D%22.format(key,%20val))ction_names.html
#
#

# Imports





##==============================================================================
##
##==============================================================================
print('\n\nexample 1')

# bad
d = {"first_name": "Alfred", "last_name":"Hitchcock"}

for key in d: print("{} = {}".format(key, d[key]))

# good
for key,val in d.items():
    print("{} = {}".format(key, val))





##==============================================================================
## Using map() or filter() where list comprehension is possible
##==============================================================================
print('\n\nexample 2')

values = [1, 2, 3]
doubles = map(lambda x: x * 2, values)
doubles = [x * 2 for x in values] # best

for key,val in d.items():
    print("{} = {}".format(key, val))





##==============================================================================
## Using an unpythonic loop
##==============================================================================
print('\n\nexample 3')
# anti pattern
l = [1,2,3]

# creating index variable
for i in range(0,len(l)):
    # using index to access list
    le = l[i]
    print(i,le)

# best practice
for i, le in enumerate(l):
    print(i, le)





##==============================================================================
## Not using zip() to iterate over a pair of lists
##==============================================================================
print('\n\nexample 4')
# anti pattern
numbers = [1, 2, 3]
letters = ["A", "B", "C"]

for index in range(len(numbers)):
    print(numbers[index], letters[index])


# best practice
numbers = [1, 2, 3]
letters = ["A", "B", "C"]

for numbers_value, letters_value in zip(numbers, letters):
    print(numbers_value, letters_value)







###==============================================================================
### Not using unpacking for updating multiple values at once
###==============================================================================
print('\n\nexample 5')

# anti pattern
def gcd(a, b):
    ''' greatest common divisor'''
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


print(gcd(10,3))

# best practice # do not use temp
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # a = b, after b updates it's value
    return a
print(gcd(10,3))

# gotchas
b = "1984"
a = b, c = "AB"
print(a)
print(b)
print(c)
