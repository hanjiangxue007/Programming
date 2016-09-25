#!/usr/bin/env python

# cmd : clear; python basics4.py

# dictionaries or hashtable or map {}

sam = {}
sam["weapon"] = "chainsaw"
sam["health"] = 10

print(sam)  # {'weapon': 'chainsaw', 'health': 10}
print(sam["weapon"])  # chainsaw

del sam["health"]
print (sam) # {'weapon': 'chainsaw'}

