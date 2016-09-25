#!/usr/bin/python


#cmd  : clear; python doubleAsteric.py


def sum(a, b):
    return a + b


# use of double asteric
# The double star ** does the same, only using a dictionary

values = { 'a': 1, 'b': 2 }
s = sum(**values)

print s
