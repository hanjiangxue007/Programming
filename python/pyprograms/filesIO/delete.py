# !/usr/bin/python

#Author: Bhishan Poudel
#topic : delete a file
#pre   : needed a file called aa.txt
#cmd   : clear; touch aa.txt
#cmd   : clear; python delete.py

import os, sys
import shutil   # to delete recursively

# create file to delete
file = open("aa.txt", "w")


# removing
os.remove("aa.txt")

print "The file aa.txt is deleted"

shutil.rmtree("test2", ignore_errors=True)

print "The dir test2 is deleted recursively"
