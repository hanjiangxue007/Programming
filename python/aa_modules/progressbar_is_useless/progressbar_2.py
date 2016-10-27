#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct 05, 2016
# Last update :
#
#
# Imports
from __future__ import division, unicode_literals, print_function

import time
import progressbar

with progressbar.ProgressBar(10) as bar:
    for i in range(10):
        time.sleep(0.1)
        bar.update(i)
