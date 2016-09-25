#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://www.datasciencebytes.com/bytes/2014/11/07/working-with-dates-in-pandas-a-few-examples/

# data
#date,temp
#11-1-2014,56
#11-2-2014,56
#11-3-2014,59
#11-5-2014,60
#11-6-2014,55

# Imports
import pandas as pd
import StringIO
import matplotlib.pyplot as plt


# for ipython %matplotlib inline
# reading as strings
df = pd.read_csv('timeseries.txt', index_col=0)
print(df)
print("\n")
#print(df.index)
print("\n")

#df.plot(marker='o', ylim=[50, 65])
#plt.ylabel("Temperature (F)")
##plt.show()


## reading txt file as date object in pandas
df = pd.read_csv('timeseries.txt', index_col=0, parse_dates=True)
#print(df.index)  # should now be a DateTimeIndex
##df.plot(marker='o', ylim=[50, 65]); plt.ylabel("Temperature (F)"); plt.show()



# padding date for nov 4, which is missing in our data
# it's also easy to add rows for missing data and fill them with NaNs or
# the last known value (pad/forward fill) or next known (back fill) value.
print(df)
print("\n")

resampled_ffill_df = df.resample('D').ffill()

print(resampled_ffill_df)  # missing data filled with last known value
