#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Sep 01, 2016
# Last update : 
#
# Run         : mpiexec -n 8 python3 size.py
#
# Outputs     : 
#
# Info:
# 1. 
#
#

# Imports
from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
print('{} {} {}'.format('\nsize = ',size, ''))

rank = MPI.COMM_WORLD.Get_rank()
print('{} {} {}'.format('rank = ',rank, ''))
