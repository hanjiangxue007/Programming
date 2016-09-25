#!/usr/bin/python

#cmd : clear; python dictmerge.py


x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
a = {'m': 4, 'a': 6}


z = x.copy()
z.update(y)

print z




# exaple 2
#=====================
z1 = dict(x.items() + y.items())

print z1





#exaple 3
#=========================================
# making a function to merge dictionaries

def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result
    
    
# using that function

z2 = merge_dicts(x,y)
print z2

z3 = merge_dicts(x,y,a) # a has most precedence

print z3
