#!/usr/bin/env python

#topic: sort
#http://zetcode.com/lang/python/dictionaries/

items = {   "coins": 7, "pens": 3, "cups": 2,
            "bags": 1, "bottles": 4, "books": 5 }

kitems = items.keys()
kitems.sort()

for k in kitems:
    print ": ".join((k, str(items[k])))

#sorting by keys
print "\nsorting keys alphabetical order"
for key in sorted(items.iterkeys()):        # using built-in sorted function
    print "%s: %s" % (key, items[key])

print "sorting keys reverse alphabetical order"

for key in sorted(items.iterkeys(), reverse=True):
    print "%s: %s" % (key, items[key])

#sorting by values
#The iteritems() function returns an iterator over the dictionary (key, value) pairs.

print "\nsorting values increasing order"
for key, value in sorted(items.iteritems(),
    key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)

print "\nsorting values decreasing order"
for key, value in sorted(items.iteritems(), # order type is controlled by the reverse parameter.
    key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)           # printing to the console

# using lambda
print "\nsorting alphabetical order "
pairs = [(1, 'orange'), (2, 'apple'), (3, 'banana'), (4, 'grapes')]

pairs.sort(key=lambda pair: pair[1])
print pairs