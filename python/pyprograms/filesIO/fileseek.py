#!/usr/bin/python

# cmd: clear; python fileseek.py

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print "10 letters of foo.txt is : ", str

# Check current position
position = fo.tell();
print "Current file position : ", position

# Reposition pointer at the beginning once again
#position = fo.seek(0, 0);
str = fo.read(10);
print "Next 10 letters are: ", str

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print "Repositioned 10 letters are: ", str


# Close opend file
fo.close()
