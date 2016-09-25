#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 18, 2016
# Ref       : http://stackoverflow.com/questions/3705670/best-way-to-create-a-reversed-list-in-python

# Imports
from __future__ import print_function


old_list = ['a', 'b']
print(old_list)
print("\n")

new_list = list(reversed(old_list))
print(new_list)
print("\n")

# It's also possible to duplicate old_list then reverse the duplicate in place:

new_list = list(old_list) # or `new_list = old_list[:]`
new_list.reverse()
print("\n")
print(new_list)


# best way
newlist = oldlist[::-1]

# The [::-1] slicing (which my wife Anna likes to call "the Martian smiley";-)
# means: slice the whole sequence, with a step of -1, i.e., in reverse.
# It works for all sequences.

# Note that this (and the alternatives you mentioned) is equivalent to a
# "shallow copy", i.e.: if the items are mutable and you call mutators on them,
# the mutations in the items held in the original list are also in the items in
# the reversed list, and vice versa. If you need to avoid that,
# a copy.deepcopy (while always a potentially costly operation),
# followed in this case by a .reverse, is the only good option.
