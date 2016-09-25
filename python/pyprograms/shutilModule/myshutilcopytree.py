#!/usr/bin/python

#ref : http://www.pythonforbeginners.com/os/python-the-shutil-module

#cmd : clear; python myshutilcopytree.py


# shutil.copytree ( src , dest )

# recursively copy the entire directory tree rooted at src to dest. 

# dest must not already exist. 

# errors are reported to standard output.


import shutil
import os

SOURCE = "samples"
BACKUP = "samples-bak"


#there MUST NOT be the backup folder already
if os.path.exists(BACKUP): shutil.rmtree(BACKUP)


# NOW we can create a backup directory
shutil.copytree(SOURCE, BACKUP)
print os.listdir(BACKUP)


