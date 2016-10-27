#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-16-2016 Sun
# Last update :
#
#
# Imports
from sunpy.sun._constants import physical_constants as pc
from sunpy.sun import constants as con


Teff = pc['effective temperature']
print('{} {} {}'.format('Teff = ',Teff, ''))
print('{} {} {}'.format('Teff.value = ',Teff.value, ''))
print('{} {} {}'.format('Teff.unit = ',Teff.unit, ''))
print('{} {} {}'.format('Teff.uncertainty = ',Teff.uncertainty, ''))


print("\n")
solar_constants = con.constants
# print(solar_constants.keys())

# ['solar flux unit', 'surface area', 'average density', 'radius', 'surface gravity', 'ellipticity', 'visual magnitude', 'center density', 'average angular size', 'absolute magnitude', 'sunspot cycle', 'effective temperature', 'aphelion distance', 'mean energy production', 'mass conversion rate', 'average intensity', 'volume', 'metallicity', 'moment of inertia', 'escape velocity', 'perihelion distance', 'GM', 'oblateness', 'mean distance', 'age', 'mass', 'luminosity', 'center temperature']
