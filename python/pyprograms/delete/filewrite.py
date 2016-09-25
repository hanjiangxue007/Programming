#!/usr/bin/python

#cmd : clear; python filewrite.py

# Open a file
fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close the file
fo.close()

print "a file foo.txt is created"

# Open the just created file
fo = open("foo.txt", "r+")
str = fo.read(10);
print "10 letters of foo.txt is : ", str
# Close opend file
fo.close()



# The write() Method

# The write() method writes any string to an 
# open file. It is important to note that 
# Python strings can have binary data and not 
# just text.

# The write() method does not add a 
# newline character ('\n') to the end 
# of the string
