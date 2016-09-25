#!/usr/bin/env python

#topic: items
#http://www.dotnetperls.com/dictionary-python

# Convert dict to list of tuples.
print "example of conversion of dict to tuples"
rents = {"apartment": 1000, "house": 1300}

rentItems = rents.items()      # note: foo = foo.items() for loop is faster method than direct foo dictinary
for x in rentItems:          # Loop and display tuple items.
    print("Place:", x[0])    # note: we cannot assign elments in tupeles
    print("Cost:", x[1])     #eg. rentItem[0] = "dorm" gives TypeError

# Items unpacking
print "\nexample of items unpacking"
data = {"a": 1, "b": 2, "c": 3}     # Create a dictionary.
for k, v in data.items():           #  here, we use the identifier "k" for the key, and "v" for the value.
   print(k, v)                      # Display key and value.

# For-loop                          # A dictionary can be directly enumerated with a for-loop
print "\nexample of for loop"
plants = {"radish": 2, "squash": 4, "carrot": 7}
for plant in plants:                # Loop over dictionary directly.
    print(plant)                    # This only accesses keys.

print                               # to access values we need to use items method
plantValues = plants.items()
for x in plantValues:
    print (x[1])

















# Description Items:
# Items. With this method we receive a list of two-element tuples. Each tuple contains,
# as its first element, the key. Its second element is the value.
#
# Tip:
# With tuples, we can address the first element with an index of 0. The second element has an index of 1.
#
# Program:
# The code uses a for-loop on the items() list. It uses the print() method with two arguments.

# Items, unpack:
# The items() list can be used in another for-loop syntax.
#     We can unpack the two parts of each tuple in items() directly in the for-loop.

# For-loop:
# A dictionary can be directly enumerated with a for-loop.
# This accesses only the keys in the dictionary. To get a value, we will need to look up the value.
#     Items:
# We can call the items() method to get a list of tuples. No extra hash lookups will be needed to access values.