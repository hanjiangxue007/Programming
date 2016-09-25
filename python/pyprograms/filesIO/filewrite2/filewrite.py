#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : https://stackoverflow.com/questions/26082718/python-write-two-lists-into-two-column-text-file

# imports
from __future__ import print_function
import numpy as np


# data
x = [1.5,15, 150, 1500]
y = [4.5,45, 450, 4500]
z = ['nepal', 'india', 'usa','china']



# write to a file
outfile = 'filewrite_np.dat'
np.savetxt(outfile, list(map(list, zip(*[x,y]))),
           fmt='%s',delimiter=' ', newline='\n')
print('{} {} {}'.format('output file : ',outfile, ''))

# transpose and write using numpy
l = [x,y,z]
l = list(map(list, zip(*l)))
print(l[0])
print(x)
outfile = 'filewrite_np1.dat'
np.savetxt(outfile, [x,y,z], fmt='%s',delimiter='\t', newline='\n')


# works for python2
## using zip and csv
#import csv
#from itertools import izip
#outfile = 'filewrite_zip.csv'
#with open(outfile, 'wb') as f:
    #writer = csv.writer(f, delimiter='\t')
    #writer.writerows(izip(x, y))

    

# general method
list1 = [ 1,2,3,4,5 ]
list2 = [ 9,8,7,6,5 ]
f = open("filewrite_python.txt", "w")
for i in range(len(list1)):
    f.write("{} {}\n".format(list1[i], list2[i]))
f.close()


# python3 way
with open('filewrite_python3.dat', 'w') as f:
    for i in range(len(list1)):
        f.write("{} {}\n".format(list1[i], list2[i]))


with open ('filewrite_python3a.txt', 'a') as f: f.write ('hi there\n')

# python3
# from __future__ import print_function  # this must be at top of the file
with open('amazing.txt', 'w') as f:
    print("hi there", file=f)
