#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 08, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#
# Ref : http://carl.cs.indiana.edu/cnets-howto/howtos/mistakes.html

# Imports
import numpy as np


# bad way
def compute(element):
    # various steps
    pass
    print(element**2)


inputdata = [1,2,3,4]
for elem in inputdata:
    compute(elem)
    
# good way
print('{} {} {}'.format('\ngood way\n','', ''))
def compute(*elements):
    for element in elements:
        # various steps
        print(element**2 )

inputdata = [1,2,3,4]
compute(*inputdata)

