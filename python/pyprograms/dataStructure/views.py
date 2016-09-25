#!/usr/bin/env python

#topic: view
#http://zetcode.com/lang/python/dictionaries/

#   Python 2.7 introduced dictionary view objects.
#   Views provide a dynamic view on the items of a dictionary.
#   When the dictionary changes, the view reflects these changes.
#   The dict.viewkeys(), dict.viewvalues() and dict.viewitems() methods return view objects.
#   A view is a virtual read-only container. A view does not make a copy of a dictionary.

fruits = { 'oranges': 12, 'pears': 5, 'apples': 4, 'bananas': 4 }

vi = fruits.viewitems()
vk = fruits.viewkeys()
vv = fruits.viewvalues()


print "\nkeys and values"       # we can remove some items using pop() method
for k, v in vi:                 # e.g. fruits.pop('apples')
    print k, v

print "\nkeys"
for k in vk:
    print k

print "\nvalues"
for v in vv:
    print v


