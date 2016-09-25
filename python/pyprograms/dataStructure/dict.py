#!/usr/bin/env python

#topic: dictionary or mapping or hashtable {"key":value, ...}
#http://www.dotnetperls.com/dictionary-python

animals = {}
animals["monkey"] = 1
animals["tuna"] = 2
animals["giraffe"] = 4

# Use in.
if "tuna" in animals:
    print("Has tuna")
else:
    print("No tuna")

# Use in on nonexistent key.
if "elephant" in animals:
    print("Has elephant")
else:
    print("No elephant")

print animals

#keys and values in dictionary
print "\nexample: keys and values in dictionary\n"

hits = {"home": 125, "sitemap": 27, "about": 43}
keys1 = hits.keys()
values1 = hits.values()

print("Keys:")
print(keys1)            # unsorted keys of dict
print(len(keys1))

print("Values:")
print(values1)
print(len(values1))

keys = sorted(hits.keys())      # sorted keys of dict
print(keys)
values1 = sorted(hits.values())      # sorted values of dict
print(values1)

