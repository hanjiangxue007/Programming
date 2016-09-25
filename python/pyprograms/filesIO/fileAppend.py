#!/usr/bin/python
#programmer: Bhishan Poudel
#cmd       : clear; python fileAppend.py

f = open('foo.txt', 'a')
f.write("line added")
f.close()


# example 2
with open("foo.txt", "a") as f:
    f.write("line added")

# open the text file and watch this

