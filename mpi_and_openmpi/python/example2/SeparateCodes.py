#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Sep 01, 2016
# Last update : 
#
# Run : mpiexec -n 4 python hello.py 
#       mpiexec -n 4 python3 hello.py
# Info:
# 1. 
#
# Ref: http://materials.jeremybejarano.com/MPIwithPython/introMPI.html

# Imports
from mpi4py import MPI


rank = MPI.COMM_WORLD.Get_rank()
print('{} {} {}'.format('\nrank = ',rank, ''))

a = 6.0
b = 3.0
if rank == 0:
        print(a + b)
if rank == 1:
        print(a * b)
if rank == 2:
        print( a*b*2)
if rank == 3:
        print(a*b*3)
if rank == 4:
        print(a*b*4)

