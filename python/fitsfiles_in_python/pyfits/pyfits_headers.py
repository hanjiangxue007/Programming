#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : https://pythonhosted.org/pyfits/

# Imports
import pyfits

hdulist = pyfits.open('input.fits')

# The open() function has several optional arguments which will be discussed in
# a later chapter. The default mode, as in the above example, is “readonly”.
# The open method returns a PyFITS object called an HDUList which is a
# list-like object, consisting of HDU objects. An HDU (Header Data Unit)
# is the highest level component of the FITS file structure, consisting of a
# header and (typically) a data array or table.

# After the above open call, hdulist[0] is the primary HDU, hdulist[1] is the
# first extension HDU (if there are any extensions), and so. It should be noted
# that PyFITS is using zero-based indexing when referring to HDUs and header
# cards, though the FITS standard (which was designed with FORTRAN in mind)
# uses one-based indexing.

# The HDUList has a useful method HDUList.info(), which summarizes the
# content of the opened FITS file:

print(hdulist.info())

#  After you are done with the opened file, close it with the HDUList.close() method:

# hdulist.close()

# The headers will still be accessible after the HDUList is closed.
# The data may or may not be accessible depending on whether the data are
# touched and if they are memory-mapped, see later chapters for detail.


# Working with FITS Headers

# As mentioned earlier, each element of an HDUList is an HDU object with .header
# and .data attributes, which can be used to access the header and data portions
# of the HDU.

# For those unfamiliar with FITS headers, they consist of a list of 80 byte
# “cards”, where a card contains a keyword, a value, and a comment.
# The keyword and comment must both be strings, whereas the value can be a
# string or an integer, floating point number, complex number, or True/False.
# Keywords are usually unique within a header, except in a few special cases.

# The header attribute is a Header instance, another PyFITS object.
# To get the value associated with a header keyword, simply do (a la Python dicts):
print("\n")
print(hdulist[0].header['NAXIS'])


#  We can also get the keyword value by indexing (a la Python lists):
print("\n")
print(hdulist[0].header[0])

#  adding keywords
prihdr = hdulist[0].header
prihdr.set('observer', 'Bhishan Poudel')

prihdr['targname'] = 'NGC121-a'
prihdr['targname'] = ('NGC121-a', 'the observation target')
print("\n")
print(prihdr['targname'])


print("\n")
print(prihdr.comments['targname'])


prihdr['history'] = 'I updated this file 2/26/09'
prihdr['comment'] = 'Edwin Hubble really knew his stuff'
prihdr['comment'] = 'I like using HST observations'
print("\n")
print(prihdr['comment'])


print("\n")
prihdr['history'][0] = 'I updated this file on 2/27/09'
print(prihdr['history'])
prihdr['comment'][1] = 'I like using JWST observations'
print(prihdr['comment'])


# To see the entire header as it appears in the FITS file (with the END card
# and padding stripped), simply enter the header object by itself,
# or print repr(header):
print("\n")
print("All headers\n")
# print(repr(prihdr))

print("\n")
print(repr(prihdr[:2]))


print(prihdr.keys())

# # =============================================================================
#  Working with Image Data
data = hdulist[0].data
print("\n")
print("Working with data\n")
print(data.shape)
print(data.dtype.name)





