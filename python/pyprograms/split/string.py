#!/usr/bin/ env python

# topic: python strings
# source: http://www.tutorialspoint.com/python/python_strings.htm

print "\nexample 1"
var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:10]  # last range is exclusive
print "Updated String :- ", var1[:6] + 'Python'

# String Special Operators
print "\nexample 2"

a = "Hello"
b = "Python"

print a + b  	# concatenation
print a * 2  	# repetition
print a[1]  	# slice
print a[1:4]  	# range slice

if "H" in a:  	# membership
    print "There is a letter H in variable a"
if "H" not in b:
    print "There is no letter H in variable b"

print "\nexample 3"
print r"that's a good news %f \n"  	# raw string

# String Formatting Operator
print "\nexample 4"

print "My name is %s and weight is %d kg!" % ('Bhishan', 71)

print "\nexample 4\n"
# triple quotes

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print para_str
print r'para_str'  # just print para_str

# Built-in String Methods
# Python includes the following built-in methods to manipulate strings

# capitalize
str1 = "hello this is bhishan"
print str1.capitalize()

# center    str.center(width, fillchar)
print str1.center(30,"a")

# count     str.count(sub, start= 0,end=len(string))
sub = "t"
print str1.count(sub,4,10)

# find    str.find(str, beg=0 end=len(string))
str2 = "is"
print str1.find(str2)
print str1.find(str2,0,4)

#split      str.split(str="", num=lines to be made)
print str1.split(' ',3)






# Symbol	Conversion

#   %c 	character
#   %s 	string conversion via str() prior to formatting
#   %i 	signed decimal integer
#   %d 	signed decimal integer
#   %u 	unsigned decimal integer
#   %o 	octal integer
#   %x 	hexadecimal integer (lowercase letters)
#   %X 	hexadecimal integer (UPPERcase letters)
#   %e 	exponential notation (with lowercase 'e')
#   %E 	exponential notation (with UPPERcase 'E')
#   %f 	floating point real number
#   %g 	the shorter of %f and %e
#   %G 	the shorter of %f and %E
#
# Other supported symbols and functionality are listed in the following table

# Symbol	    Functionality
#   *	        argument specifies width or precision
#   -	        left justification
#   +	        display the sign
#   <sp>	    leave a blank space before a positive number
#   #	        add the octal leading zero ( '0' ) or hexadecimal leading
#           '0x' or '0X', depending on whether 'x' or 'X' were used.
#   0	        pad from left with zeros (instead of spaces)
#   %	        '%%' leaves you with a single literal '%'
#   (var)	    mapping variable (dictionary arguments)
#   m.n.	    m is the minimum total width and n is the number of digits
#           to display after the decimal point (if appl.)
