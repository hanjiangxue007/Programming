#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016
# Ref       : http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python

# Imports
from tempfile import mkstemp
from shutil import move
from os import remove, close
import fileinput

# method 1,  this does not wrap inside (), it very good.
#==============================================================================
def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


file_path = 'b.txt'
pattern = '300.2'
subst = 'hello'

replace(file_path, pattern, subst)


## method 2
##==============================================================================
##import fileinput
#filename = 'b.txt'
#for line in fileinput.input(filename, inplace = 1):
      #print (line.replace("300.3", "hi"),)




