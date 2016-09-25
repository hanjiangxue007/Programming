#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016
# Ref       : http://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import fileinput


infile = 'replace_line.txt'


#==============================================================================
## read in a file
#with open(infile, 'r') as f:
    ## read a list of lines into data
    #data = f.readlines()

## now change the 2nd line, note that you have to add a newline
#data[1] = 'changed line 2' + '\n'

## and write everything back
#with open('replace_line.txt', 'w') as f:
    #f.writelines( data )
#==============================================================================





# method 2 (this loads whole file into the memory
#==============================================================================
def replace_line(infile, line_num, text):
    lines = open(infile, 'r').readlines()
    lines[line_num] = text
    out = open(infile, 'w')
    out.writelines(lines)
    out.close()

# edit third line
#replace_line(infile, 2, 'changed line 3')





#==============================================================================
# using fileinput

#for  line in fileinput.FileInput(infile, inplace=1):
    ##if line.startswith('#'):
        ##print (line.rstrip('\n'))

    ##line = line.replace("line", "row")
    ##print(line.rstrip('\n'))

    # replace every occurences of "old" substring to "new" substring
    #print (line.rstrip().replace('1', '10'),)



## replace line 3
#i = 0
#replaced_line = 'replaced line'
#for  line in fileinput.FileInput(infile, inplace=1):
    #if i ==2:
        #print(replaced_line.rstrip('\n'),)
    #else:
        #print(line.rstrip())
        
    #i += 1


    
## replace line index 6 to 10
i = 0
replaced_line = 'replaced line_index'
for  line in fileinput.FileInput(infile, inplace=1):
    if ( 6 <= i <= 10):
        txt = replaced_line + '_{:d}'.format(i)
        print(txt.rstrip('\n'),)
        
    else:
        print(line.rstrip('\n'))
        
    i += 1






