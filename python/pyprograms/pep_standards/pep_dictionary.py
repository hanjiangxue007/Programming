#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 10, 2016
# Last update :
#





##==============================================================================
## Not using dict comprehensions
##==============================================================================
# anti pattern
numbers = [1,2,3]

# hard to read
my_dict = dict([(number,number*2) for number in numbers])

print(my_dict)  # {1: 2, 2: 4, 3: 6}


##==============================================================================
# best practice
numbers = [1, 2, 3]

my_dict = {number: number * 2 for number in numbers}

print(my_dict)  # {1: 2, 2: 4, 3: 6}
