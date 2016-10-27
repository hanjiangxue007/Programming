#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-10-2016 Mon
# Last update :
#
# Ref: http://pint.readthedocs.io/en/0.7.2/systems.html?highlight=units
#
# Imports
import pint
ureg = pint.UnitRegistry(system='mks')

print(ureg.default_system) #


q = 3600. * ureg.meter / ureg.hour
print(q.to_base_units())


ureg.default_system = 'cgs'
print(q.to_base_units())


ureg.default_system = 'imperial'
print('{:.3f}'.format(q.to_base_units()))
'1.094 yard / second'

ureg.default_system = 'mks'
print(ureg.get_compatible_units('meter'))


ureg.default_system = 'imperial'
print(ureg.get_compatible_units('meter'))

# You can check which unit systems are available:
print("\n")
print(dir(ureg.sys.mks))

print("\n")
print(dir(ureg.sys.imperial))
#['UK_hundredweight', 'UK_ton', 'acre_foot', 'cubic_foot', 'cubic_inch',
# 'cubic_yard', 'drachm', 'foot', 'grain', 'imperial_barrel',
# 'imperial_bushel', 'imperial_cup', 'imperial_fluid_drachm',
# 'imperial_fluid_ounce', 'imperial_gallon', 'imperial_gill',
# 'imperial_peck', 'imperial_pint', 'imperial_quart', 'inch',
# 'long_hunderweight', 'long_ton', 'mile', 'ounce', 'pound', 'quarter',
# 'short_hunderdweight', 'short_ton', 'square_foot', 'square_inch',
# 'square_mile', 'square_yard', 'stone', 'yard']

