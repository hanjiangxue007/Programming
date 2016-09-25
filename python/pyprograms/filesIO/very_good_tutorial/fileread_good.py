#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016
# Ref       : http://www.computerhope.com/issues/ch001721.htm 

# Imports
from __future__ import print_function




# python --version
# python3 --version

##=============================================================================
in_file = open("lorem.txt", "rt") # open file lorem.txt for reading text data (rt =read text)
contents = in_file.read() # read the entire file into a string variable
in_file.close() # close the file
#print(contents) # print contents







##=============================================================================
# using with
with open ('lorem.txt', 'rt') as in_file: # Open file lorem.txt for reading of text data.
    contents = in_file.read()# Read the entire file into a variable named contents.
    #print(contents) # Print contents. 










##=============================================================================
# Reading Text Files Line-By-Line
with open ('lorem.txt', 'rt') as in_file: # Open file lorem.txt for reading of text data.
    for line in in_file: # Store each line in a string variable "line"
        #print(line) # prints that line, print also add one newline
        pass 









##=============================================================================
# Reading Data Into A Variable
# Declare an empty list named "lines"
# Open file lorem.txt for reading of text data.
# For each line of text, store it in a string variable named "line", and
# add that line to our list of lines. print(lines) # print the list object. 

lines = [] 
with open ('lorem.txt', 'rt') as in_file:    
    for line in in_file:
        lines.append(line)        
        
#print(lines[0])










##=============================================================================
# if we have already newline, end=""
lines = [] # Declare an empty list named "lines"

with open ('lorem.txt', 'rt') as in_file: # Open file lorem.txt for reading of text data.
    for line in in_file: # For each line of text in in_file, where the data is named "line",
        lines.append(line) # add that line to our list of lines.
    for element in lines: # For each element in our list,
        #print(element,end="") # print it.
        pass 









##=============================================================================
# stripping newlines from data,and then print
lines = [] # Declare an empty list named "lines"
with open ('lorem.txt', 'rt') as in_file: # Open file lorem.txt for reading of text data.
    for line in in_file: # For each line of text in in_file, where the data is named "line",
        lines.append(line.rstrip('\n')) # add that line to our list of lines, stripping newlines.
    for element in lines: # For each element in our list,
        #print(element) # print it.
        pass









##=============================================================================
# Searching For Substrings Using A String's find() Method

#print(lines[0])
#print(lines[0].find("V"))
#print(lines[0].find("e", 5)) # start from 6th character








##=============================================================================
# Working With Multiple Lines Of Text
# Enumerate objects don't have a printable form on their own,
# but we can use the list() function to create a list of our enumerate object

# The enumerate object creates a sequence of tuples from our list.

#print(lines)
#print(list(enumerate(lines)))

for linenum, line in enumerate(lines):
    #print(linenum, line)











