#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 11, 2016
# Last update :
#

# Imports
import scipy.constants as const
import scipy.constants as const


# get in-built values
print('c = ', const.c)

# use dictionary
value, unit, precision = const.physical_constants['Bohr magneton']
print(value,unit,precision)


#print(const.find('bohr'))
print(const.find('proton'))




#amu_to_MeV, _, _ = const.physical_constants['atomic mass constant energy equivalent in MeV']

#E_Be8 = ndat.atomic_mass('Be8') * amu_to_MeV
#E_alpha = ndat.atomic_mass('He4') * amu_to_MeV
#print(E_Be8 - 2*E_alpha, 'MeV') # prints 0.09183948326 MeV
