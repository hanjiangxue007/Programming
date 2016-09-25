#!/usr/bin/python

#ref : http://www.pythonforbeginners.com/os/python-the-shutil-module

#cmd : clear; python myshutilrmtree.py


# shutil.rmtree ( path )

# recursively delete a directory tree.




# This removes the directory 'three' and anything beneath it in the filesystem.
import shutil
import os

path = 'one/two/three'


#optional: we can create a folder first to delete it recursively

# if not os.path.exists(path): os.makedirs(path)


# now we can delete the path

# aliter: if os.path.exists('one/two/three'):
if os.path.exists(path):
    shutil.rmtree(path)
    
    
print 'The path everything inside folder three is deleted if the folder exists'
