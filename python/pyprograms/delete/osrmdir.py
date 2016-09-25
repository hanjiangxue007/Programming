#!/usr/bin/python

#cmd : clear; python osrmdir.py

import os

# This would  remove "/tmp/test"  directory.
#os.rmdir( "/tmp/test"  )
if os.path.exists("test2"):  # deletes only empty folder
    os.rmdir( "test2"  )
