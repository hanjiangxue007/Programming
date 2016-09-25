#!/usr/bin/python

#ref : http://www.pythonforbeginners.com/os/python-the-shutil-module

#cmd : clear; python myshutilmove.py

import shutil
import os


# create some files in the source
fo = open("test/hello.txt", "wb")

#define file and destination
file = "test/hello.txt"
destination = "test3"

# we MUST delete the destination if it already exists
if os.path.exists(destination): shutil.rmtree(destination)


#create a new empty destination
os.makedirs(destination)

#now, we can move to newly created destination
shutil.move(file,destination)



# recreate the moved files in the source
fo = open("test/hello.txt", "wb")

print "Look inside the destination: ", destination



# shutil.move

# recursively move a file or directory (src) to another location (dst).

# if the destination is a directory or a symlink to a directory,
# then src is moved
# inside that directory.

# the destination directory must not already exist.

# this would move files ending with .txt to the destination path

# if destination folder is already present it will show
# raise Error, "Destination path '%s' already exists" % real_dst
