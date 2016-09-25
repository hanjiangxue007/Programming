#!/usr/bin/python

# cmd : clear; python splitMethod.py

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( )       # this will ignore new line, 3 items in the list
print str.split(' ', 1 ) # this will print new line , 2 items in the list
