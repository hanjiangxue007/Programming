#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 10, 2016
# Last update :
#





##==============================================================================
## Not using dict keys when formatting strings
##==============================================================================

# anti pattern
person = {
    'first': 'Tobin',
    'age':20
}

print('{0} is {1} years old'.format(
    person['first'],
    person['age'])
)
# Output: Tobin is 20 years old

person = {
    'first': 'Tobin',
    'last': 'Brown',
    'age':20
}

# Bad: we have to change the replacement fields within
# our string, once we add new values
print('{0} {1} is {2} years old'.format(
    person['first'],
    person['last'],
    person['age'])
)  # bad
# Output: Tobin Brown is 20 years old


##==============================================================================
# better
person = {
    'first': 'Tobin',
    'age':20
}

print('{first} is {age} years old'.format(**person))
# Output: Tobin is 20 years old

person = {
    'first':'Tobin',
    'last': 'Brown',
    'age':20
}
print('{first} {last} is {age} years old'.format(**person))
# Output: Tobin Brown is 20 years old

##==============================================================================
# best
class Person(object):

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return '{first} {last} is {age} years old'.format(**self.__dict__)


person = Person('Tobin', 'Brown', 20)
print(person)
# Output: Tobin Brown is 20 years old
