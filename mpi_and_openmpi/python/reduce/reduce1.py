#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 23, 2016
# Last update :
#

# Imports
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

val = 3
sum = comm.reduce(val, op=MPI.SUM, root =0)

if rank == 0:
    print ("The reduction sum is %s" % sum)


# Reduce takes all the values sent by each process and
# performs a reduction operation on them.

# ans is 12


max = comm.reduce(rank, op=MPI.MAX, root =0)

if rank == 0:
    print ("The reduction max is %s" % max)
