#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://scipython.com/book/chapter-6-numpy/examples/using-numpys-loadtxt-method/
# Execute   : python3 numpy_loadtxt_1.py


# Imports
import numpy as np
import matplotlib.pyplot as plt



fname = 'F3V'
dtype1 = np.dtype([('wave', 'f8'), ('flux', 'f8')])
a = np.loadtxt(fname, dtype=dtype1, skiprows=57, usecols=(0,1))
nlines = len(a)
print('{} {} {} {}'.format('\nnlines      = ', nlines,'',''))
print('{} {} {} {}'.format('a[0]        = ', a[0],'\na[len(a)-1] = ', a[len(a)-1]))

# print height array
#print(a['wave'])

# data
wave = a['wave']
flux = a['flux']

#plt.plot(wave,flux)
#plt.show()

##=============================================================================
wv,flx = np.loadtxt(fname, dtype=(float,float),
         skiprows=0, usecols=(0,1),unpack=True,delimiter=None)
print('{} {} {} {}'.format('\nwv = ', wv,'','\n'))

plt.plot(wv,flx)
plt.show()
##=============================================================================



