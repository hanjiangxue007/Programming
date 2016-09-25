#!/usr/bin/env python
## topic : IndexError: list index out of range

# wrong method

n = [3,5,7]

def myFun(x):
    for i in x:
        print x[i]   # x[3],x[5],x[7] are all out of list

myFun(n)            # IndexError: list index out of range

# correct method
n = [3,5,7]

def myFun(n):
    for i in range(0,3):
        print n[i]
myFun(n)


# correct method2
print
n = [3,5,7]

def myFun(x):
    for i in x:
        print i   # it should be print i , x[3],x[5],x[7] are all out of list

myFun(n)