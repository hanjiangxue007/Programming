#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct 06, 2016
# Last update :
#
#
# Imports
from __future__ import division, unicode_literals, print_function

from visual import *
s = sphere(color=color.cyan)

def change():
    if s.color == color.cyan:
        s.color = color.red
    else:
        s.color = color.cyan

scene.bind('click', change)
