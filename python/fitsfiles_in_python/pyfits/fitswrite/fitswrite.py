#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://pythonhosted.org/pyfits/



# imports
import numpy as np
import os
import pyfits as py

# data
data1  = np.arange(40).reshape(10,4)
data2 = 2 * data1
data3 = 4* data1
print(data1)
print('{} {} {} {}'.format('\ndata[0] = ', data1[0],'is first row','\n'))
#data1[0][0] = 10 first pixel change


# Next, we create a PrimaryHDU object to encapsulate the data:
hdu1 = py.PrimaryHDU(data1)
hdu2 = py.PrimaryHDU(data2)
hdu3 = py.PrimaryHDU(data3)


print("\n")
outfile1 = 'out1.fits'
outfile2 = 'out2.fits'
outfile3 = 'out3.fits'

if os.path.isfile(outfile1):
    print('{} {} {} {}'.format('Warning: \ndeleting the file: ', outfile1, '',' \n' ))
    os.remove(outfile1)

if os.path.isfile(outfile2):
    print('{} {} {} {}'.format('Warning: \ndeleting the file: ', outfile2, '',' \n' ))
    os.remove(outfile2)

if os.path.isfile(outfile3):
    print('{} {} {} {}'.format('Warning: \ndeleting the file: ', outfile3, '',' \n' ))
    os.remove(outfile3)



hdu1.writeto(outfile1)
hdu2.writeto(outfile2)
hdu3.writeto(outfile3)
# This will write a single HDU to a FITS file without having to
# manually encapsulate it in an HDUList object first.
print('{} {} {} {}'.format('\nOutput file = ', outfile1,outfile2,outfile3))
