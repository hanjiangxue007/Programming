#!/usr/bin/python

# note: The method tell() returns the current
#        position of the file read/write pointer
#        within the file.
# cmd : clear; python filetell.py

# Open a file
fo = open("foo.txt", "rw+")
print "Name of the file: ", fo.name

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline()
print "Read Line: %s" % (line)

# Get the current position of the file.
pos = fo.tell()
print "Current Position: %d" % (pos)

# Close opend file
fo.close()
