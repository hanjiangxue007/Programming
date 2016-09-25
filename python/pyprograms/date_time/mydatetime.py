#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 12, 2016

# note: datetime.timedelata has only three attributes d.days d.seoncds, d.microseconds


# Imports
import datetime

t = datetime.time(1, 2, 3)
print (t)
print(('hour  :', t.hour))
print(('minute:', t.minute))
print(('second:', t.second))
print(('microsecond:', t.microsecond))
print(('tzinfo:', t.tzinfo))


##=============================================================================
print('{} {} {}'.format('\n\n','', ''))

today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year:', today.year)
print('Mon :', today.month)
print('Day :', today.day)



##=============================================================================
seconds = 86400*2 + 60.1

m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print("\nTime taken : {0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

print ("\n%d:%02d:%02d" % (h, m, s))


##=============================================================================
print('{} {} {}'.format('\n\n','', ''))
seconds = 86400*2 + 60.1
d = datetime.timedelta(seconds=seconds)

print('Time taken : {} days {} hours {} minutes {} seconds {} microseconds'.format(d.days,d.seconds//3600, d.seconds//60,d.seconds, d.microseconds))

