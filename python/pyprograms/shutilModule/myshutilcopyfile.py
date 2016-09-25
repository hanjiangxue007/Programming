#!/usr/bin/python

#ref : http://www.pythonforbeginners.com/os/python-the-shutil-module

#cmd : clear; python myshutilcopyfile.py



import shutil  
shutil.copyfile('test/hello.txt', 'test/folder2/newhello.txt')

print "Look inside the destination\n"
print "Note: for shutil.copyfile both names are file\n"


# shutil.copyfile ( src , dest )

# copy data from src to dest 

# both names must be files.

# copy files by name 

