#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct 05, 2016
# Last update :
#
# Ref: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
#
# Imports
from __future__ import division, unicode_literals, print_function
from time import sleep
from random import random
from clint.textui import progress

if __name__ == '__main__':
    for i in progress.bar(range(100)):
        sleep(random() * 0.2)

    for i in progress.dots(range(100)):
        sleep(random() * 0.2)
