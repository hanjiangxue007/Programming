#!/usr/bin/env python

# cmd : clear; python basics7.py

print "now we will study exceptions handling"
# x = 5 + "bag"
# print x

try:
    x = 5 + "bag"
except:
    print "error of adding number and string"

print  "**********************************************"
print "now we will study pass"
y = 5
try:
    y = 6 + "sam"
except:
    pass

print y



#print  "**********************************************"
#print "now we will study raise" \
#      ""
#raise TypeError("youGotTypingError")
#z = 6 + "sam"
#print z

print  "**********************************************"
print "error finally"
try:
    x = 5 + "sam"
except ZeroDivisionError:
    print "will not see this"
finally:
    print "the final word"
    
print  "**********************************************"
print
