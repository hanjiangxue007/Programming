#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : https://docs.python.org/2/library/sets.html
# Ref       : https://en.wikibooks.org/wiki/Python_Programming/Sets


# set of integers
my_set = {1, 2, 3}

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}

# set donot have duplicates
#{1,2,3,4,3,2}
#{1, 2, 3, 4}

# set cannot have mutable items
my_set = {1, 2, [3, 4]}

#TypeError: unhashable type: 'list'

# but we can make set from a list
set([1,2,3,2])
#{1, 2, 3}






























from sets import Set
engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers           # union
engineering_management = engineers & managers            # intersection
fulltime_management = managers - engineers - programmers # difference
engineers.add('Marvin')                                  # add element
print engineers 

employees.issuperset(engineers)     # superset test

employees.update(engineers)         # update from another set
employees.issuperset(engineers)

for group in [engineers, programmers, managers, employees]: 
    group.discard('Susan')          # unconditionally remove element
    print group



# example 2
# https://en.wikibooks.org/wiki/Python_Programming/Sets
print("\n\n")


set1 = set()                   # A new empty set
set1.add("cat")                # Add a single member
set1.update(["dog", "mouse"])  # Add several members
if "cat" in set1:              # Membership test
  set1.remove("cat")
#set1.remove("elephant") - throws an error
set1.discard("elephant")       # No error thrown
print (set1)
print("\n")


for item in set1:              # Iteration AKA for each element
  print item
print "Item count:", len(set1) # Length AKA size AKA item count
isempty = len(set1) == 0       # Test for emptiness
set1 = set(["cat", "dog"])     # Initialize set from a list
set2 = set(["dog", "mouse"])
set3 = set1 & set2             # Intersection
set4 = set1 | set2             # Union
set5 = set1 - set3             # Set difference
set6 = set1 ^ set2             # Symmetric difference
issubset = set1 <= set2        # Subset test
issuperset = set1 >= set2      # Superset test
set7 = set1.copy()             # A shallow copy
set7.remove("cat")
set8 = set1.copy()
set8.clear()                   # Clear AKA empty AKA erase
print (set1, set2, set3, set4, set5, set6, set7, set8, issubset, issuperset)
