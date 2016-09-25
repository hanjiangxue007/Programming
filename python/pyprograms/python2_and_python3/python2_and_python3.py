#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np



# Character is not same as binary string in python 3
# python3 python2_and_python3.py
print('\nb prefix is for byte strings.')
print(b'A' == b'\x41') # True
print('A' == b'A')     # True for python2 and False for python3



# Python 3.x makes a clear distinction between the types:

# str   = '...' literals = a sequence of Unicode characters
#         (UTF-16 or UTF-32, depending on how Python was compiled)
# bytes = b'...' literals = a sequence of octets
#         (integers between 0 and 255)

# A CHARACTER IS NOT A BYTE. That idea is long obsolete.

# In order to ease the 2.x-to-3.x transition, the b'...' literal syntax
# was backported to Python 2.6, in order to allow distinguishing binary strings
# (which should be bytes in 3.x) from text strings (which should be str in 3.x).
# The b prefix does nothing in 2.x, but tells the 2to3 script not to convert
# it to a Unicode string in 3.x.
