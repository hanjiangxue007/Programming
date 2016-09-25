#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016
# Ref     : http://xahlee.info/python/python3_string_formatting.html

# Imports
from __future__ import division
from __future__ import print_function


#Convert data into string format.

#repr() → convert a data into a string form that can be
#read back into Python or for eval()
#str() → convert into a string in a human readable form.

ss = [3, 4, 3.123456789012345678901234567890, (7, 8, "9")]
print (str(ss))         # [3, 4, 3.1234567890123457, (7, 8, '9')]
print (repr(ss))        # [3, 4, 3.1234567890123457, (7, 8, '9')]


# integer
print("%d" % (1234))             # 「1234」

# padding by space
print("%4d" % (12))              # 「  12」

# float. 2 integer, 4 decimal
print("%2.4f" % (3.123456789))   # 「3.1235」

# string.
print("%5s" % ("cats"))          # 「 cats」
print("%2s" % ("cats"))          # 「cats」

print("%2d◇%6d◇%2.4f◇%s" % (1234, 5678, 3.123456789, 'cats!')) # 「1234◇  5678◇3.1235◇cats!」


# using format
print("\n")
print("{}".format("cat"))       # cat
print("I have {} cats and {} dogs.".format(3,4)) # I have 3 cats and 4 dogs.

# use {{}} to include literal {}
print("brace {{}}, a is {}".format(3))     # brace {}, a is 3

# format codes
print("\n")
# “:s” is for string
print("{:s}".format("cat"))          # cat
# decimal int
print("{:d}".format(3))          # 3
# binary
print("{:b}".format(3))          # 11
# hex
print("{:x}".format(10))          # a
# formatting multiple args
print("{:d}, {:s}, {:s}".format(3, "cat", [7, 8]))


# argument order
print("\n")
print("{0:d}, {1:s}, {2:s}".format(3, "cat", [7, 8])) # 3, cat, [7, 8]
print("{1:s}, {0:d}, {2:s}".format(3, "cat", [7, 8])) # cat, 3, [7, 8]

# Format number in human readable format:
print("\n")
print("{:,}".format(78515573)) # 78,515,573
