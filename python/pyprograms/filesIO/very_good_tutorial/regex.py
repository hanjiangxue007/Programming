#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016
 

# Imports
from __future__ import print_function
import re


# char 	meaning
# \b 	A word boundary matches an empty string (anything, including nothing at all),
#       but only if it appears before or after a non-word character. "Word characters"
#       are the digits 0 through 9, the lowercase and uppercase letters,
#       or an underscore ("_").
# 
# d 	Lowercase letter d.
# \w* 	\w represents any word character, and * is a quantifier meaning "zero
#       or more of the previous character." So \w* will match zero or more word characters.
#
# r 	Lowercase letter r.
# \b 	Word boundary.



##=============================================================================
str = "Good morning, doctor." # string to search
pat = re.compile(r"\bd\w*r\b") # compile the regex "\bd\w*r\b" into a pattern object
if pat.search(str) != None: # Search for the pattern. If the result is NOT false,
    #print("Found it.") # report a positive result.
    pass




##=============================================================================
# ignore case
str = "Hello, DoctoR." # String has a capital D and R,
pat = re.compile(r"\bd\w*r\b", re.IGNORECASE) # but it will match because the pattern ignores case
if pat.search(str) != None:
    print("Found it.")
    pass












##=============================================================================
# Search a dictionary for words
# The program below searches the dictionary for any words that start with d and end in r. 
filename = "/usr/share/dict/words"
pattern = re.compile(r"\bd\w*r\b", re.IGNORECASE)
with open(filename, "rt") as in_file:
    for line in in_file:
        if pattern.search(line) != None:
            #print(line, end='')
            pass
