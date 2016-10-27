#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-09-2016 Sun
# Last update :
#
#
# Imports
from pint import UnitRegistry
u = UnitRegistry()
ureg = UnitRegistry()


distance = 24.0 * u.meter
print(distance) # 24.0 meter


mytime = 8.0 * u.second
print(mytime) # 8.0 second
print(repr(mytime))

##======================================================================
print("\n")
print(distance.magnitude) # 24.0
print(distance.units) # meter
print(distance.dimensionality) #[length]


##======================================================================
print("\n")
speed = distance / mytime
print(speed) # 3.0 meter / second

speed.to(u.inch / u.minute )
print(speed) # return same

# return inplace
speed.ito(u.inch / u.minute )
print(speed)





##======================================================================
## to_base_units
##======================================================================
print("\n")
height = 5.0 * u.foot + 9.0 * u.inch
print(height) # 5.75 foot

print(height.to_base_units()) # 1.7526 meter
print(height) # 5.75 foot

height.ito_base_units()
print(height) # 1.7526 meter





##======================================================================
## to(ureg.meter) etc
##======================================================================
print("\n")
distance = 42 * ureg.kilometers
print(distance) # 42 kilometer
print(distance.to(ureg.meter)) # 42000.0 meter
