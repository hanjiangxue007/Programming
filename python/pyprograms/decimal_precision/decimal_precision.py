#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 21, 2016
# Ref       : https://gist.github.com/jackiekazil/6201722

# Imports
from __future__ import print_function
import numpy as np
import decimal
from decimal import Decimal
from decimal import Decimal, ROUND_HALF_UP
from decimal import getcontext, Decimal


# best method
value = 8.123456789
value = float(str(round(value, 1)))
print(value)
print(value + 0.0000000003)


# example2
value = 1.000000000000001
addme = 0.1234567890123456789
print('{} {} {}'.format('value = ',value, ''))
print('{} {} {}'.format('addme = ',addme, ''))
print('{} {} {}'.format('value + addme = ',value + addme, ''))


##==============================================================================
# examples
print (16.0/7)  # 2.28571428571
# First we take a float and convert it to a decimal
x = Decimal(16.0/7)

# Then we round it to 2 places
output = round(x,2)
print (output)



