#!/usr/bin/ env python

#string split method for strings :
# str.split(str="", num=string.count(str))

str = "Line1-abcdef Line2-abc main\tLine4-abcd"
print str.split()           # default: splits at whitespaces and escape charcters are applied
print str.split(" ", 2)     # splitted on whitespace and number of splits = 2+1
print str.split(" ", 0)     # splitted on whitespace and number of splits = 0+1

temp = str.split("-")
print
print temp
print temp[0]               # Line1
print temp[1]               # abcdef Line2
print temp[2]               # abc main (and in tab) Line4
print temp[3]               # abcd
#print temp[4]              # IndexError: list index out of range

#example 2
print "\nexample 2:"
line ="pix_scale=0.03"      # pixel scale to use (arseconds per pixel)

temp = line.split("=")      # splitted at = then, we have temp[0] and temp[1]
print temp[0], temp [1]

#Description

#The method split() returns a list of all the words in
# the string, using str as the separator (splits on all
# whitespace if left unspecified), optionally limiting
# the number of splits to num.