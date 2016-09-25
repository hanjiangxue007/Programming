#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 23, 2016
# Ref       : http://effbot.org/librarybook/fileinput.htm 

# Imports
from __future__ import print_function
import fileinput
import sys
import glob
import string


##=============================================================================
for line in fileinput.input("samples/sample.txt",inplace=False, mode='r'):
    sys.stdout.write("-> ")
    sys.stdout.write(line)





##=============================================================================

for line in fileinput.input(glob.glob("samples/*.txt")):
    if fileinput.isfirstline(): # first in a file?
        sys.stderr.write("\n-- reading %s --\n" % fileinput.filename())
    sys.stdout.write(str(fileinput.lineno()) + " " + string.upper(line))





##=============================================================================

