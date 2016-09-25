#!/usr/bin/python

#ref  : https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean-in-python?lq=1

#cmd  : clear; python mixedAsteric.py



# use of double asteric
# The double star ** does the same, only using a dictionary

values = { 'a': 1, 'b': 2 }
s = sum(**values)

print s



def sum(a, b, c, d):
    return a + b + c + d

values1 = (1, 2) # tuple will need single *
values2 = { 'c': 10, 'd': 15 } # dict will need double **
s = sum(*values1, **values2)

print s
