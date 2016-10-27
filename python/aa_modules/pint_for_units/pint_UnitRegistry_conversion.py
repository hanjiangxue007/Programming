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
ureg = UnitRegistry()


distance = 1 * ureg.au
print(distance.to(ureg.m))
