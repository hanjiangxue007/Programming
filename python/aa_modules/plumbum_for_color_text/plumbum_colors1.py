#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct 06, 2016
# Last update :
#
# Ref: https://github.com/tomerfiliba/plumbum
#
# Imports
from __future__ import division, unicode_literals, print_function
from plumbum import colors
with colors.red:
    print("This library provides safe, flexible color access.")
    print(colors.bold | "(and styles in general)", "are easy!")
print("The simple 16 colors or",
      colors.orchid & colors.underline | '256 named colors,',
      colors.rgb(18, 146, 64) | "or full rgb colors",
      'can be used.')
print("Unsafe " + colors.bg.dark_khaki + "color access" + colors.bg.reset + " is available too.")
