#!/usr/bin/env python
from math import pi, sin

print"\neg1: sum of first 10-1 numbers"
print sum (i for i in range(10))			# 9 * 10/2 = 45

print "\neg2: sum of squares of numbers upto 10-1"
print sum(i*i for i in range(10))                 # sum of squares

print "\neg3: dot product of two list"
xvec = [10, 20, 50]
yvec = [1, 2, 4]
print sum(x*y for x,y in zip(xvec, yvec))         # dot product

print "\neg4: printing sine table\n"  # range 0 to 180, interval 30
sine_table = dict((x, sin(x*pi/180)) for x in range(0, 180,30))
print sine_table

print "\neg5: reverse of a string"
data = 'i love u'			#	in the output: read from right to left
print list(data[i] for i in range(len(data)-1,-1,-1))
print
