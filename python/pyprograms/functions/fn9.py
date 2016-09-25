#!/usr/bin/env python
## topic: function returning absolute value

def distance_from_zero(s):
    if type(s) == type(1) or type(s) == type(1.2):
        print ("absolute value is: "), abs(s)
        return abs(s)
    else:
        print ("This is not a number")
        return s
        
distance_from_zero(-1.234)
distance_from_zero("hello")

b=1
c = distance_from_zero(-2)
print b+c

d = "Hello"
e = distance_from_zero("World")
print d+e
