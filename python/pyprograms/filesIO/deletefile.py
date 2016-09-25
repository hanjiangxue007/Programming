#Author: Bhishan Poudel
#ref   : http://www.tutorialspoint.com/python/os_remove.htm

#pre   : create a file aa.txt
#cmd  : clear; python deletefile.py

# !/usr/bin/python

import os, sys

# listing directories
print "The dir is: %s" %os.listdir(os.getcwd())

# removing
os.remove("aa.txt")

# listing directories after removing path
print "The dir after removal of path : %s" %os.listdir(os.getcwd())
