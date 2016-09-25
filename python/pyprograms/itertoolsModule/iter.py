#!/usr/bin/python

#cmd  : clear; python iter.py

import itertools

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)
print(list(itertools.permutations(horses)))
