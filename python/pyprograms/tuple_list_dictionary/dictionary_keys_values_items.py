#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016


# Imports
#from __future__ import division
#from __future__ import print_function



d={'key1':'value1','key2':'value2','key3':'value3'}
print (d.keys())    # will give you all keys in list ['a','b']
print (d.values())  # will give you values in list ['apple','ball']
print (d.items())   # will give you pair tuple of key and value

# print dictionary key value pairs
for key, value in d.iteritems(): print (key, ':', value)
#    python2  ('key3', ':', 'value3')
#    python3   key3 = value3

# print keys in newlines (for future)
#print(*d, sep='\n')

# display better for python2
d={'a':1,'b':2,'c':3}
for kv in d.items(): print kv[0],':',kv[1]
