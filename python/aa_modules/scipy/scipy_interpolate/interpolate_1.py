#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author  : Bhishan Poudel 
# Date    : May 23, 2016
# Ref     : https://stackoverflow.com/questions/16070219/how-to-interpolate-points-in-a-specific-interval-on-a-plot-formed-by-loading-a-t 
# Ref     : https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html


# Imports 
import numpy as np
import scipy as sp
from scipy import interpolate


data = np.genfromtxt('data.txt')

x = data[:,0]  #first column
y = data[:,1]  #second column




xnew = [600,800,750]

#f = interpolate.interp1d(x, y)
#ynew = f(xnew)   # use interpolation function returned by `interp1d`


ynew = interpolate.interp1d(x, y, kind='cubic') (xnew)

print(ynew[0])  # 2.65731978328e-11


# inside F3V
#1.239748    2.65739e-11    2.22158e-14
#1.240071     2.6573e-11    2.23646e-14



# If you want to smooth your data, you can use the univariatespline,
# just replace the f = interpolate... line with:

# f = interpolate.UnivariateSpline(x, y)

# To change how much it smooths, you can fiddle with the s and k options:

#f = interpolate.UnivariateSpline(x, y, k=3, s=1)
