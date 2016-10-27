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


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("hello world from process ", rank)


