#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://scipython.com/book/chapter-6-numpy/examples/using-numpys-loadtxt-method/
# Execute   : python3 numpy_loadtxt_1.py


# Imports
import numpy as np



fname = 'eg6-a-student-data.txt'
dtype1 = np.dtype([('gender', '|S1'), ('height', 'f8')])
a = np.loadtxt(fname, dtype=dtype1, skiprows=9, usecols=(1,3))
nlines = len(a)
print('{} {} {} {}'.format('\nnlines      = ', nlines,'',''))
print('{} {} {} {}'.format('a[0]        = ', a[0],'\na[len(a)-1] = ',
                    a[len(a)-1]))

# To find the average heights of the male students, we only want to index
# the records with the gender field as M, for which we can create a boolean array:

m = a['gender'] == bytes('M')
print('{} {} {} {}'.format('\nm= \n ', m,'','\n'))


# m has entries that are True or False for each of the 19 valid records
# (one is commented out) according to whether the student is male or female.
# So the heights of the male students can be seen to be:

print(a['height'][m])

m_av = a['height'][m].mean()
f_av = a['height'][~m].mean()
print('Male average: {:.2f} m, Female average: {:.2f} m'.format(m_av,f_av))



##=============================================================================
# To perform the same analysis on the student weights we have a bit more work to
# do because there are some missing values (denoted by '-'). We could use np.
# genfromtxt (see Section 6.2.3 of the book), but let's write a converter
# method instead. We'll replace the missing values with the nicely unphysical
# value of -99. The function parse_weight expects a string argument and returns
# a float:

def parse_weight(s):
    try:
        return float(s)
    except ValueError:
        return -99.

# This is the function we want to pass as a converter for column 4:

dtype2 = np.dtype([('gender', '|S1'), ('weight', 'f8')])
b = np.loadtxt(fname, dtype=dtype2, skiprows=9, usecols=(1,4),
                       converters={4: parse_weight})

# Now mask off the invalid data and index the array with a boolean array as before:
mv = b['weight'] > 0    # elements only True for valid data
m_wav = b['weight'][mv & m].mean()      # valid and male
f_wav = b['weight'][mv & ~m].mean()     # valid and female
print('Male average: {:.2f} kg, Female average: {:.2f} kg'.format(m_wav,f_wav))








##=============================================================================
# note:
print('\n\n\nb prefix is for byte strings.')
print(b'A' == b'\x41') # True
print('A' == b'A')     # True for python2 and False for python3
