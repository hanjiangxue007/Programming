#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 12, 2016
 

# Imports
import numpy as np

seconds = 100.1

m, s = divmod(seconds, 60)
print(m,s)

h, m = divmod(m, 60)
print(h,m)


d, h = divmod(h, 24)
print(d,h)
