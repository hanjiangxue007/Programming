#!/usr/bin/python

# cmd : clear; python fileObjectAttributes.py
# Syntax:
# file object = 
# open(file_name [, access_mode][, buffering])
# modes: r rb r+ w wb w+ wb+ a ab a+ ab+

# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

# Attribute	    Description
# file.closed	Returns true if file is closed,
#               false otherwise.
#file.mode	    Returns access mode with 
#               which file was opened.
#file.name	    Returns name of the file.
#file.softspace	Returns false if space
#               explicitly required with print,
#               true otherwise.
