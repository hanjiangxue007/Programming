#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 12, 2016

# Imports
import datetime

def GetTime(sec):
    sec = datetime.timedelta(seconds=float(sec))
    d = datetime.datetime(1,1,1) + sec

    #print("DAYS:HOURS:MIN:SEC")
    #print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))
    print("Time taken : {0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.3f} seconds.".format(
    d.day, d.hour, d.minute, d.second))


GetTime(1.2)




##=============================================================================

t = 1.2
day= t//86400
hour= (t-(day*86400))//3600
minit= (t - ((day*86400) + (hour*3600)))//60
seconds= t - ((day*86400) + (hour*3600) + (minit*60))
print( day, 'days' , hour,' hours', minit, 'minutes',seconds,' seconds')
