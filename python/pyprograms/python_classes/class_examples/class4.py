#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 07, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#
#

class MyClass(object):
    ## No need for dot syntax
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var

## Need dot syntax as we've left scope of class namespace
print(MyClass.class_var) ## 1

foo = MyClass(2)
print(foo.i_var) # Finds i_var in foo's instance namespace

## Doesn't find class_var in instance namespace…
## So look's in class namespace (MyClass.__dict__)
print(foo.class_var) ## 1

# accessing values
foo = MyClass(2)
print(foo.class_var) ## 1
foo.class_var = 2    # assign class_var attribute to the instance only
print(foo.class_var) # 2
print(MyClass.class_var) ## 1
##====================================================================

# example 2
print("\nExample 2\n")
class MyClass(object):
    limit = 10

    def __init__(self):
        self.data = []

    def item(self, i):
        return self.data[i]

    def add(self, e):
        if len(self.data) >= self.limit:
            raise Exception("Too many elements")
        self.data.append(e)

print(MyClass.limit)
foo = MyClass()
foo.limit = 50
## foo can now hold 50 elements—other instances can hold 10

##====================================================================
## mutable attributes inside a class
print('{} {} {}'.format('\nExample 3\n','', ''))
class Person(object):
    all_names = []

    def __init__(self, name):
        self.name = name
        Person.all_names.append(name)

joe = Person('Joe')
bob = Person('Bob')
print (Person.all_names)
## ['Joe', 'Bob']

##====================================================================
## Private instance variables
print("\nExample of private instance variables")
class Bar(object):
    def __init__(self):
        self.__zap = 1

a = Bar()
#print(a.__zap)
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
## AttributeError: 'Bar' object has no attribute '__baz'

## Hmm. So what's in the namespace?
print(a.__dict__)  # {'_Bar__zap': 1}
print(a._Bar__zap) # 1

# description:
# this behavior is largely intended to help out with subclassing. 
# In the PEP 8 style guide, they see it as serving two purposes: 
# (1) preventing subclasses from accessing certain attributes, 
# and (2) preventing namespace clashes in these subclasses. 
# While useful, variable mangling shouldn’t be seen as an
# invitation to write code with an assumed public-private
# distinction, such as is present in Java.



