#!/usr/bin/python

#ref : https://stackoverflow.com/questions/5082452/python-string-formatting-vs-format

#cmd : clear; python format4.py


class A(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
            

a = A(2,3)


# use of positional argument
print 'x is {0.x}, y is {0.y}'.format(a)

print 'x is {0}, y is {1}'.format(a.x, a.y)



# use a keyword argument instead of positional argument
print 'x is {a.x}, y is {a.y}'.format(a=a)

#note: This example is not possible with % specifier

