#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author  : Bhishan Poudel 
# Date    : May 23, 2016
# Ref     : https://stackoverflow.com/questions/11851770/spline-interpolation-with-python

# Imports 
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d

x1 = [1., 0.88,  0.67,  0.50,  0.35,  0.27,  0.18,  0.11,   0.08,   0.06,   0.04,   0.02]
y1 = [0., 13.99, 27.99, 41.98, 55.98, 69.97, 83.97, 907.97, 111.96, 125.96, 139.95, 153.95]

# Combine lists into list of tuples
points = zip(x1, y1)

# Sort list of tuples by x-value
points = sorted(points, key=lambda point: point[0])

# Split list of tuples into two list of x values any y values
x1, y1 = zip(*points)

print(len(x1),len(y1))
print("\n")

for i in range(0,len(x1)):
	print(x1[i], y1[i])

new_length = 10
new_x = np.linspace(min(x1), max(x1), new_length)
new_y = sp.interpolate.interp1d(x1, y1, kind='cubic')(new_x)

print("\n")
for i in range(0,new_length-1):
	print(new_x[i], new_y[i])


