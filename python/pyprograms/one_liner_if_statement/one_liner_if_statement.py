#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 01, 2016
# Ref       : https://stackoverflow.com/questions/2802726/putting-a-simple-if-then-statement-on-one-line 

# Imports
import numpy as np


# using one liner in python, is UNPYTHONIC and bad way

# exaple 1
print('{} {} {}'.format(r'example 1 ','', ''))
for i in range(3): print ("Here's i: "); print (i)
#for i in range(3): if i % 2: print "That's odd!"  # IMPOSSIBLE




# example 2
print('{} {} {}'.format('\nexample 2','', ''))
x=10
while x > 0: print (x); x-=1

# x=10; while x > 0: print x; x-=1 # IMPOSSIBLE



# example 3
print('{} {} {}'.format('\nexample 3','', ''))
if "exam" in "example": print ("yes!")


# example 4
print('{} {} {}'.format('\nexample 4','', ''))
def squared(x): return x * x
print(squared(5))



# example 5
print('{} {} {}'.format('\nexample 5','', ''))
x = 5
a = 1 if x > 15 else 2
print(a)



# example 6
print('{} {} {}'.format('\nexample 6','', ''))
N = 2
for count in range(5):
    count = 0 if count == N else N+1
    print(count)


    
# example 7
print('{} {} {}'.format('\nexample 7','', ''))
N = 2
for count in range(5):
    count = [0,N+1][count==N]
    print(count)

    
# example 8
print('{} {} {}'.format('\nexample 8','', ''))
N = 2
for count in range(5):
    count = [lambda:0, lambda:N+1][count==N]()
    print(count)

    
# example 9
print('{} {} {}'.format('\nexample 9','', ''))
N = 2
for count in range(5):
    count == (count + 1) % N
    print(count)



