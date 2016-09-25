#!/usr/bin/python

#Topic: print function in python

#cmd  : clear; python prints.py


print "Let's study this example:\n"

#example2

string = 'Bhishan Poudel'
print "The person's name is: ", string


my_name = 'Bhishan Poudel'
my_age = 30 # not a lie
my_height = 66 # inches
my_weight = 170 # lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about '%s':\n" % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print "Thanks for reading this information\n"
