#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 


# Imports
#from itertools import count
#def gen_filenames(prefix, suffix, places=3):
    #"""Generate sequential filenames with the format <prefix><index><suffix>

       #The index field is padded with leading zeroes to the specified number of places
    #"""
    #pattern = "{}{{:0{}d}}{}".format(prefix, places, suffix)
    #for i in count(1):
        #yield pattern.format(i)

#g = gen_filenames("data_", ".dat")

#for x in range(3):
    #print(next(g))




# method 2
#from itertools import count
#filename = ("data_%03i.dat" % i for i in count(1))
#next(filename)
## 'data_001.dat'
#next(filename)
## 'data_002.dat'
#next(filename)
## 'data_003.dat'

# method 3
filename = []
for i in range(10):
    tmp = 'data_%d.dat'%(i,)
    filename.append(tmp)
print (filename[0])
