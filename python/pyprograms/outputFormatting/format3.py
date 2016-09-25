#!/usr/bin/python

#ref : https://stackoverflow.com/questions/5082452/python-string-formatting-vs-format

#cmd : clear; python format3.py


#!/usr/bin/python
sub1 = "python string!"
sub2 = "an arg"

a = "i am a %s" % sub1
b = "i am a {0}".format(sub1)

c = "with %(kwarg)s!" % {'kwarg':sub2}
d = "with {kwarg}!".format(kwarg=sub2)

print a    # "i am a python string!"
print b    # "i am a python string!"
print c    # "with an arg!"
print d    # "with an arg!"


#example2

name = 'Bhishan Poudel'
name2 = (1, 2, 3) # a tuple



print "hi there %s" % name

#print "hi there %s" % name2  # this doesnot work
print "hi there %s" % (name2,)



# str.format gives more functionalities
