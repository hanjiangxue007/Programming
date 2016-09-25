#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 08, 2016
# Last update :
#
# Inputs      : none
#
# Outputs     :
#
# Info:
# 1.
#
#

# Imports
import re

# how one would normally do it
def contains_foobar_1(s):
    return "foobar" in s.lower()

# how one does it with regex, properly
def contains_foobar_2(s):
    return re.search(r'foobar', s, flags = re.IGNORECASE) is not None

# how one does it with regex
# (trying to squeeze every bit of efficiency outta it)
_foobar_re = re.compile(r'foobar', flags = re.IGNORECASE)
def contains_foobar_3(s):
    return _foobar_re.search(s) is not None


if __name__ == '__main__':
    a = contains_foobar_1('Foobar is a string')
    print(a)



