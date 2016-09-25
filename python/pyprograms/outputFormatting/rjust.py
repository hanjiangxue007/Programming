#!/usr/bin/python

#ref : https://docs.python.org/2/tutorial/inputoutput.html

#cmd : clear; python rjust.py


for x in range(1, 11):
     print repr(x).rjust(2), repr(x*x).rjust(3),
     # Note trailing comma on previous line
     print repr(x*x*x).rjust(4)
     
     
#example 2
print "\nexample2\n"
for x in range(1,11):
     print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
     
     
     
     
#     (Note that in the first example, one space between each 
#     column was added by the way print works: it always adds 
#     spaces between its arguments.)

#    This example demonstrates the str.rjust() method of string 
#    objects, which right-justifies a string in a field of a 
#    given width by padding it with spaces on the left
