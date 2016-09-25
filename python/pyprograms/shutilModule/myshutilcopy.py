#!/usr/bin/python

#ref : http://www.pythonforbeginners.com/os/python-the-shutil-module

#cmd : clear; python myshutilcopy.py

# NOTE: The shutil module offers a number of high-level 
#       operations on files and collections of files


# shutil. copy ( src , dest )

# Basically the unix command cp src dst. 

# this copies the source file to the destination directory

# the destination directory has to exist

# if the filename already exists there, it will be overwritten

# access time and last modification time will be updated

# the same filename is used

# the permissions of the file are copied along with the contents.


import shutil
import os
source = os.listdir("/tmp/")
destination = "/tmp/newfolder/"
for files in source:
    if files.endswith(".txt"):
        shutil.copy(files,destination)

print "Look inside destination"












# Some of the functions inside shutil module are follwing:
#-------------------------------------------------------------------------
#| Function          |Copies Metadata|Copies Permissions|Can Specify Buffer|
#-------------------------------------------------------------------------
#| shutil.copy       |      No       |        Yes       |        No        |
#-------------------------------------------------------------------------
#| shutil.copyfile   |      No       |         No       |        No        |
#-------------------------------------------------------------------------
#| shutil.copy2      |     Yes       |        Yes       |        No        |
#-------------------------------------------------------------------------
#| shutil.copyfileobj|      No       |         No       |       Yes        |
#-------------------------------------------------------------------------

#copy2 is also often useful, it preserves the original modification 
#and access info (mtime and atime) in the file metadata.
