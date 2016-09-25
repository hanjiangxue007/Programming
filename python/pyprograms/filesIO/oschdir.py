#!/usr/bin/python

#cmd : clear; python oschdir.py

import os

# Changing a directory to "/home/newdir"
os.chdir("/home/bhishan/newdir")

# make a new directory there
if not os.path.exists("test"):
    
    os.mkdir("test")

print "A new directory called test is created"
print "inside /home/bhishan/newdir"


