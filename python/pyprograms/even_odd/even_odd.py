#!/usr/bin/python
# -*- coding: utf-8 -*-

# Bhishan Poudel
# Feb 9, 2016

# method 1 using modulo operator
#num = int(input("Enter a number: "))
num = 6
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

####################################   
# method 2 using &
def even_odd(x):
    if x & 1:
       return 'odd'
    else:
       return 'even'
a = even_odd(5)
print(a)


