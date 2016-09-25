#!/usr/bin/python

# cmd  : clear; python myshutilcopy2.py

#NOTE: if there is a file called shutil.py in any directory,
#      it will show import error, so always rename it.

import shutil
shutil.copy2('test/hello.txt', 'test2/newhello.txt')

print "Look inside the destination directory"







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
