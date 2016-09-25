#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author  : Bhishan Poudel 
# Date    : May 23, 2016
# Ref     : https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html

# Imports 
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

import numpy as np
import scipy as sp
from scipy.interpolate import interp1d


x = [1., 0.88,  0.67,  0.50,  0.35,  0.27, 0.18,  0.11,  0.08,  0.04,  0.04,  0.02]
y = [0., 13.99, 27.99, 41.98, 55.98, 69.97, 83.97, 97.97, 111.96, 125.96, 139.95, 153.95]

## if we sort x, y values will not be corresponding value
#x = sorted([1., 0.88, 0.67, 0.50, 0.35, 0.27, 0.18, 0.11, 0.08, 0.04, 0.04, 0.02])
#y = [0., 13.99, 27.99, 41.98, 55.98, 69.97, 83.97, 97.97, 111.96, 125.96, 139.95, 153.95]

# so, we can use reverse values
x = x.reverse()
y = y.reverse()


new_x = [0.25,5.0,7.5]
new_y = sp.interpolate.interp1d(x, y, kind='cubic')(new_x)
print(new_y)


# here x1 and y1 are monotonically decreasing, we can also use x1 = x1.reverse()

