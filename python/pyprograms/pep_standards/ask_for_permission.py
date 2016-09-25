#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 10, 2016
# Last update :
#


##==============================================================================
## Asking for permission instead of forgiveness
##==============================================================================
# anti pattern

import os

# violates EAFP coding style
if os.path.exists("file.txt"):
    os.unlink("file.txt")


# best practice
try:
    os.unlink("file.txt")
# raised when file does not exist
except OSError:
    pass
