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
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


# now write you print, wait a second, logger function
logger.debug('This is for debugging. Very talkative!')
logger.info('This is for normal chatter')
logger.warning('Warnings should almost always be seen.')
logger.error('You definitely want to see all errors!')
logger.critical('Last message before a program crash!')
