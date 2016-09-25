#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 17, 2016
# Ref       : http://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file
# http://stackoverflow.com/questions/4454298/prepend-a-line-to-an-existing-file-in-python



# Imports
import os,shutil,fileinput


# In mode 'a' or 'a+' , any writing is done at the end of the file,
# even if at the current moment when the write() function is triggered the
# file's pointer is not at the end of the file: the pointer is moved to the
# end of file before any writing. You can do what you want in two manners.
#==============================================================================


# Python2:
#filename = 'a1.txt'
#with file(filename, 'r') as original: data = original.read()
#with file(filename, 'w') as modified: modified.write("new first line\n" + data)

##Python3:
#with open(filename, 'r') as original: data = original.read()
#with open(filename, 'w') as modified: modified.write("new first line\n" + data)


# method 2
# This does the job without reading the whole file into memory,
# though it may not work on Windows


# using a function
# this deletes first file and creates new, if interrupted, we will lose the data
def prepend_line(path, line):
    with open(path, 'r') as old:
	os.unlink(path)
	with open(path, 'w') as new:
	    new.write(str(line) + "\n")
	    shutil.copyfileobj(old, new)


# function
path = 'a1.txt'
line = '#added text'
prepend_line(path, line)
