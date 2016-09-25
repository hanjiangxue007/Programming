# !/usr/bin/python

#Author: Bhishan Poudel
#topic : delete a file
#pre   : needed a file called aa.txt
#cmd   : clear; touch aa.txt
#cmd   : clear; python delete.py

import os, sys, errno
import shutil   # to delete recursively


########################################################
# remvoing a FILE
# create file to delete
filename="a.tmp"
file = open(filename, "w")
os.remove(filename)  # os.remove("test2/aa.txt")     # this will delet file inside test2
print "The file",filename,"is deleted"


# delete if file exists(path.exists)
filename="b.tmp"
file = open(filename, "w")
if os.path.exists(filename):
    os.remove(filename)
    
print "The file",filename,"is deleted"

# delete if file exists(path.isfile)
# os.path.exists returns True for folders as well as files
filename="c.tmp"
file = open(filename, "w")

if os.path.isfile(filename):
    os.remove(filename)
    print "The file",filename,"is deleted"

# delete if file exists(method 2)
filename="d.temp"
file = open(filename, "w")
try:
    os.remove(filename)
except OSError:
    pass
print "The file",filename,"is deleted"

# delete if file exists(using function)
filename="e.temp"
file = open(filename, "w")

def silentremove(filename):
        try:
            os.remove(filename)
        except OSError as e: # this would be "except OSError, e:" before Python 2.6
            if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
                raise # re-raise exception if a different error occured
                
              
silentremove(filename)
print "The file",filename,"is deleted"


###########################################################
# removing EMPTY FOLDER

if os.path.exists("test2"):  # deletes only empty folder
    os.rmdir( "test2"  )

############################################################


###########################################################
# removing NON EMPTY FOLDER

shutil.rmtree("test2", ignore_errors=True)
print "The probably non-empty folder 'test2' is deleted"

############################################################
