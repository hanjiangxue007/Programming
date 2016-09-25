#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 26, 2016
# Ref       : http://stackoverflow.com/questions/14340283/how-to-write-to-a-specific-line-in-file-in-python

# Imports
from __future__ import print_function

#==============================================================================
# insert a line between two lines
infile = 'input'
outfile = 'output'
with open(infile) as fin, open(outfile,'w') as fout:
    for line in fin:
        fout.write(line)

	line_before = 'xxxxx' +'\n'
        if line == line_before:
           next_line = next(fin)

	   line_after = 'yyyyy' + '\n'
           if next_line == line_after:
	       line_insert = 'my_line' + '\n'
               fout.write(line_insert)
           fout.write(next_line)
#==============================================================================








# for small file
with open("input") as f,open("out.txt",'w') as o:
    data=f.read()
    old_lines = "xxxxx" + '\n' + "yyyyy"
    new_lines = "xxxxx" + "\n" + "yourline" + "\n" + "yyyyy"
    data=data.replace(old_lines,new_lines)
    o.write(data)
