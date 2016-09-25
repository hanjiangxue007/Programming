#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 12, 2016
 

# Imports
import sys

class Tee(object):
    """
    Allow forking of output to stdout and other files.
    """
    def __init__(self, *files):
        self.files = files
    
    def open(self):
        """ Redirect stdout """
        if not hasattr(sys, '_stdout'):
            # Only do this once just in case stdout was already initialized
            # @note Will fail if stdout for some reason changes
            sys._stdout = sys.stdout
        sys.stdout = self
        return self

    def close(self):
        """ Restore """
        stdout = sys._stdout
        for f in self.files:
            if f != stdout:
                f.close()
        sys.stdout = stdout
    
    def write(self, obj):
        for f in self.files:
            f.write(obj)

if __name__ == '__main__':
    print ("Start...")
    t = Tee(sys.stdout, open('test.txt', 'w')).open()
    print ("Hello world")
    t.close()
    print ("Goodbye")

"""
[ bash ]
$ python tee.py 
Start...
Hello world
Goodbye
$ cat /tmp/test.txt 
Hello world
"""
