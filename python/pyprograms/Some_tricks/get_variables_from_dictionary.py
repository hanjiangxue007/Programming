#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 10, 2016
# Last update :
#
# Depends     : none
#
# Outputs     :
#
# Info:
# 1. WARNING: It is not a good idea to create variables dynamically
#
#





# mydict
mydict = {'a':'foo', 'b':2}


## method1
#for key,val in mydict.items():
        #exec(key + '=val')
#print(a)


## method2
#a, b = mydict['a'], mydict['b']
#print(b)


# method 3  bad idea
locals().update(mydict)
#print(a)


# good idea 17k
class Bunch(object):
    def __init__(self, adict):
        self.__dict__.update(adict)

d = {'a':1, 'b':2}
vars = Bunch(d)
#print (vars.a, vars.b)

# unpythonic but works
d = dict(param='hello', param2=500, param3=[1,2,3])

for k, v in d.items():
    exec ('%s = v' % k)


print(param,param3)
