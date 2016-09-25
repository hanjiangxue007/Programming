#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 10, 2016
# Last update :
#

print ({i : chr(65+i) for i in range(4)})


key_list,value_list = ['a', 'b', 'c'], [1,2,3]
d = {(key, value) for (key, value) in zip(key_list, value_list)}

print(d)
