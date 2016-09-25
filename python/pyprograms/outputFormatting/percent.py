#!/usr/bin/python

#ref : https://docs.python.org/2/library/stdtypes.html#string-formatting

#cmd : clear; python percent.py

print '%(language)s has %(number)03d quote types.' % \
       {"language": "Python", "number": 2}
 
 
#output: Python has 002 quote types.

# The '%' character marks the start of the specifier.
# (language) is a Mapping key (optional)
# the first flag 0 means padding with zeros
# the next  flag 3d means three digit long      
       





#    A conversion specifier contains two or more characters 
#    and has the following components, which must occur in 
#    this order:

# 1    The '%' character, which marks the start of the specifier.
# 2    Mapping key (optional), consisting of a parenthesised 
#     sequence of characters (for example, (somename)).
#    
# 3    Conversion flags (optional), which affect the result of 
#      some conversion types.
# 4    Minimum field width (optional). If specified as an '*' (asterisk), 
#     the actual width is read from the next element of the tuple in values, 
#     and the object to convert comes after the minimum field width and 
#     optional precision.
#    
# 5    Precision (optional), given as a '.' (dot) followed by the precision. 
#     If specified as '*' (an asterisk), the actual width is read from the 
#     next element of the tuple in values, and the value to convert comes 
#     after the precision.
# 6   Length modifier (optional).
# 7   Conversion type.


# Conversion flags characters are: # 0 - space +
# Conversion types are           : d i o u x X e E f F g G c s %
# Length modifiers are           : h l L (Python ignores them hd and d are same)
