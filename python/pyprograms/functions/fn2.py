#!/usr/bin/env python
#author: bhishan poudel
#cmd   : clear; python fn2.py


import copy

def changeme( foo ):

    foo.append([1,2,3,4])

    return


mylist = [10,20,30]
mylist2 = copy.deepcopy(mylist)

a = changeme( mylist )

print mylist            # my list is changed, output: [10, 20, 30, [1, 2, 3, 4]]

print changeme(mylist)  # output: None

print a                 # output: None

print mylist2           # output: [10, 20, 30]
