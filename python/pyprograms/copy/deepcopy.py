#!/usr/bin/env python

# cmd : python deepcopy.py

import copy


#copying a list
# without using shallow copy


print
colors1 = ["red", "green"]
print "original colors1:", colors1
colors2 = colors1
print "colors2 = colors1"
colors2[1] = "blue"
print "colors2[1] = blue "
print "changed colors1:",colors1


# using deepcopy
print
colors3 = ["cyan", "yellow"]
print "original colors3:", colors3
colors4 = copy.deepcopy(colors3)
print "colors4 = copy.deepcopy(colors3)"
colors4[1] = "magenta"
print "colors4[1] = magenta"
print "unchanged colors3:",colors3
print "changed colors4:",colors4
print
