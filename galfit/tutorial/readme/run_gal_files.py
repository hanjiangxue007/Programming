#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 08, 2016


# Imports
import os

for file in os.listdir('.'):
    if os.path.splitext(file)[1] == ".gal":
        os.system("galfit %s" % file)

