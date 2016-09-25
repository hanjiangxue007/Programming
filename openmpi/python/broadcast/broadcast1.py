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
if rank == 0:
    fd = open("dna_file.txt", "r")
    dna = fd.read()
else:
    dna = None

dna = comm.bcast(dna, root=0)
print (rank, dna)


# Broadcast

# Useful when one process has data that all the other processes need to know.

# For example, we have a program that works with a dna string stored in a file.

# One way to share the dna string among the processes is to read the dna
# string from proccess 0, and then broadcast the string to the other processes.
