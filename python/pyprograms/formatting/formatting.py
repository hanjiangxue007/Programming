#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 09, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#
#

# Imports
capital_country = {"United States" : "Washington", 
                   "US" : "Washington", 
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    print("{}: {}".format(c, capital_country[c]))
    
    
    
# example 2
print("{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
#'Spam & Eggs:           6.99'

print("{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
#'        Spam & Eggs:   6.99'

print("{0:>20s} {1:6.2f}".format('Spam & Ham:', 7.99))
#'         Spam & Ham:   7.99'

print("{0:<20s} {1:6.2f}".format('Spam & Ham:', 7.99))
#'Spam & Ham:            7.99'

print("{0:<20} {1:6.2f}".format('Spam & Ham:', 7.99))
#'Spam & Ham:            7.99'

print("{0:>20} {1:6.2f}".format('Spam & Ham:', 7.99))

##==============================================================
print('{} {} {}'.format('\nPadding with 0','', ''))
x = 378
print("The value is {:06d}".format(x))
#The value is 000378

x = -378
print("The value is {:06d}".format(x))
#The value is -00378

##==============================================================
print('{} {} {}'.format('\nThousands separator','', ''))
x = 78962324245
print("The value is {:,}".format(x))
#The value is 78,962,324,245

print("The value is {0:6,d}".format(x))
#The value is 5,897,653,423

x = 5897653423.89676
print('            ', x)
print("The value is {0:12,.3f}".format(x))
#The value is 5,897,653,423.897
