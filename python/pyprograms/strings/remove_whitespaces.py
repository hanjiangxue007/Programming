#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 08, 2016
# Ref       : https://stackoverflow.com/questions/959215/removing-starting-spaces-in-python 

# Imports
import re
import string


# best
s = " \t foo \n bar "
b = "".join(s.split())   # best
c = s.replace(" ", "")  # only space, no others
d = re.sub(r"\s", "", s)
#print(c)
print(d)


# example
word = '  Hello World  '
wordModified = word.lstrip().rstrip()
print(wordModified)


# example
li = [" 0", " 1", " 2"]
li = list(map(str.lstrip,li))
print(li)


# example
a = [" 0", " 1", " 2"]
b = [s.lstrip() for s in a]
print(b)

# example
a = re.sub(r'\s+', '', '  strip my spaces  ')
print(a)


# example
word = '  Hello World  '
#re.sub(r'^[^a]*', word)
d = re.sub(r'^[^e]*', "", word)
print(d)