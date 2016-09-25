#!/usr/bin/python

#ref : https://stackoverflow.com/questions/5082452/python-string-formatting-vs-format

#cmd : clear; python format2.py

tu = (0,11,22,33,44)
print '{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu)
print


#          {0} {2} {1} {2} {3} {2} {4} {2}
# result : 0    22 11  22  33  22  44  22




#    Another point: format(), being a function, can be used as an argument
#    in other functions: 

li = [12,45,78,784,2,69,1254,4785,984]
print map('the number is {}'.format,li)   

print

from datetime import datetime,timedelta

once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
delta = timedelta(days=13, hours=8,  minutes=20)

gen =(once_upon_a_time +x*delta for x in xrange(20))

print '\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen))
