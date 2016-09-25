#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : 2016-07-07
# Ref       : http://stackoverflow.com/questions/8113782/split-string-on-whitespace-in-python
 

# Imports
import re
import string


# example
s = "many   fancy word \nhello    \thi"
mylist = re.findall(r'\S+', s)
print(mylist[0])


# example
mystr = "many   fancy word \nhello    \thi"
string_list = mystr.split()
print(string_list)

# example
mystr = "hello world sample text".split()
mystr = "hello world sample text".split(" ")
mystr = re.split(" +", "hello world sample text")


# example
text = "'Oh, you can't help that,' said the Cat: 'we're all mad here. I'm mad. You're mad.'"
a = text.split()
print(a[0])

# example
a =  [word.strip(string.punctuation) for word in text.split()]
print(a[0])

# example
text = r"object 0 0.0 0.0 15 ../../Research/twenty_catalogs/seds/broadband.sed 0 0 0 0 0 0 star none none"
a =  text.split()[5].split("/")[5]
print(a) # broadband.sed

# example
a = "It was love at first sight".split()
print(a)
