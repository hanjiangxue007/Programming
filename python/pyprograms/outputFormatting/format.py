#!/usr/bin/python

#ref : https://docs.python.org/2/tutorial/inputoutput.html

#cmd : clear; python format.py

print 'I am  {} from "{}!"'.format('Bhishan Poudel', 'Nepal')

#   The objects inside {}, called format fields, are
#   replaced with the objects passed into the .format method


#use of positional arguments
print '{0} and {1}'.format('Bhishan', 'eggs')
print '{1} and {0}'.format('Bhishan', 'Poudel')


#use of keyword arguments
print 'This {food} is {adjective}.'.format(
       food='guacamoli', adjective='absolutely horrible')


#mixed use
print 'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                    other='George')


#  '!s' (apply str()) and '!r' (apply repr()) can be
#    used to convert the value before it is formatted.

import math
print 'The value of PI is approximately {}.'.format(math.pi)
print 'The value of PI is approximately {!r}.'.format(math.pi)


#    An optional ':' and format specifier can follow the field name.
#    This allows greater control over how the value is formatted.
#    The following example rounds Pi to three places after the decimal.

print 'The value of PI is approximately {0:.3f}.'.format(math.pi)
print 'The value of PI is approximately %.2f.' % math.pi

#next example
print
table = {'Bhishan': 4127, 'Poudel': 4098, 'Nepal': 8637678}
print ('Poudel: {0[Poudel]:d}; Bhishan: {0[Bhishan]:d}; '
        'Nepal: {0[Nepal]:d}'.format(table))


print
table = {'Bhishan': 4127, 'Poudel': 4098, 'Nepal': 7678}
for name, phone in table.items():
     print '{0:10} ==> {1:10d}'.format(name, phone)


print
table = {'Bhishan': 4127, 'Poudel': 4098, 'Nepal': 8637678}
print 'Poudel: {Poudel:d}; Bhishan: {Bhishan:d}; Nepal: {Nepal:d}'.format(**table)
