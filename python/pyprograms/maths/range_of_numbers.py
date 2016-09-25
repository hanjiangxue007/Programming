#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016
 

# Imports
import numpy as np


# numbers between two values
start = 531.0
end = 696.0
step = (end-start) / 20.0

# make decimal precision 1
step = float(str(round(step, 1)))
print('{} {} {}'.format('start = ',start, 'nm'))
print('{} {} {}'.format('end = ',end, 'nm'))
print('{} {} {}'.format('step = ',step, ' nm\n'))

breakpoints = np.arange(start,end,step)
breakpoints = np.append(breakpoints, end)

print('{} {}{}'.format('breakpoints = \n', breakpoints,'' ))
print('{} {}{}'.format('\nlen breakpoints = ', len(breakpoints),'' ))



