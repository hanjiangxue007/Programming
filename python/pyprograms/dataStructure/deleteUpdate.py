#!/usr/bin/env python

#topic: DELETE, UPDATE, COPY, FROMKEYS, DICT, GET methods in dictionary
#http://www.dotnetperls.com/dictionary-python

# delete method to remove a dictionary entry
print ("delete method for dictionary entries")
systems = {"mac": 1, "windows": 5, "linux": 1}  #we initialize a dictionary with three key-value tuples.
print(systems)
del systems["windows"]      # Remove key-value at "windows" key.
print(systems)

# update method to change one dictionary to have new values from a second dictionary

print ("\nupdate method for dictionary entries")
pets1 = {"cat": "feline", "dog": "canine"}
pets2 = {"dog": "animal", "parakeet": "bird"}
pets1.update(pets2)
print(pets1)
print(pets2)
mypets1 = sorted(pets1.keys())
print (mypets1)

# copy method in dictionary
print ("\ncopy method for dictionary entries")
original = {"box": 1, "cat": 2, "apple": 5}
modified = original.copy()          # shallow copy
modified["cat"] = 200
modified["apple"] = 9
print(original)
print(modified)

# fromkeys method in dictionary:   dict.fromkeys(name_of_key, value_of_key)
print ("\nfromkeys method for dictionary entries")
keys = ["bird", "plant", "fish"]      # A list of keys.
print "keys=", keys
d = dict.fromkeys(keys, 5)            # Create dictionary from keys.
print "dictionary=", d

# dictionary from a list of tuples
print ("\ndictionary from a list of tuples")    # We create list of tuple pairs.
pairs = [("cat", "meow"), ("dog", "bark"), ("bird", "chirp")]   # ... These are key-value pairs.
lookup = dict(pairs)                    # Convert list to dictionary.
print(lookup.get("dog"))
print(len(lookup))

# get method in dictonary
print "\nget method in dictonary"
letters = "abcabcdefghi"    # The first three letters are repeated.
frequencies = {}
for c in letters:
    frequencies[c] = frequencies.get(c, 0) + 1

for f in frequencies.items():
        print(f)        # Print the tuple pair.

