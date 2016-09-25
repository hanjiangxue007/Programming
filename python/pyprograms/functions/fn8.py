#!/usr/bin/python
## topic: function with absolute value


a = -5.36
b = "story"

print type(a)
print type (b)
print type (1)
print type ("hello")

print abs(a)

if type (a) == type ("hello"):
    print "both are same type"
else: 
    print "both are different type"
   

def myfunc(s):
    if type(s) == type (1):
        print ("it's an integer")
    elif type(s) == type (1.1):
        print ("it's a float")
    elif type(s) == type ("hello"):
        print ("it's a string")
    else:
        print ("its unknown item")
print        
myfunc("hello") # invoking function
myfunc(4)
myfunc(-4.5)

