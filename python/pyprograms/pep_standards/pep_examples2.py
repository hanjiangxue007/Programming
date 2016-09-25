#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 10, 2016
# Last update :
#





##==============================================================================
## Not using named tuples when returning more than one value from a function
##==============================================================================

# anti pattern
def get_name():
    return "Richard", "Xavier", "Jones"

name = get_name()

# no idea what these indexes map to!
print(name[0], name[1], name[2])

# best practice
from collections import namedtuple

def get_name():
    name = namedtuple("name", ["first", "middle", "last"])
    return name("Richard", "Xavier", "Jones")

name = get_name()

# much easier to read
print(name.first, name.middle, name.last)






##==============================================================================
##
##==============================================================================

