#!/usr/bin/python

#cmd : clear; python fileopen.py

# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name

# Close opend file
fo.close()
