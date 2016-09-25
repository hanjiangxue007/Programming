#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016
# Ref       : http://www.tutorialspoint.com/python/file_writelines.htm

# Imports
from __future__ import print_function
import numpy as np


# Open a file in witre mode
fo = open("foo.txt", "rw+")
print ("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

seq = ["This is 6th line\n", "This is 7th line"]
# Write sequence of lines at the end of the file.
fo.seek(0, 2)
line = fo.writelines( seq )

# Now read complete file from beginning.
fo.seek(0,0)
for index in range(7):
   line = fo.next()
   print ("Line No %d - %s" % (index, line),end='')

# Close opend file
fo.close()
