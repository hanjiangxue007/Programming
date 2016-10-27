#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 23, 2016
# Last update :
#

# Imports
from mpi4py import MPI

comm = MPI.COMM_WORLD   # Defines the default communicator
num_procs = comm.Get_size()  # Stores the number of processes in size.
rank = comm.Get_rank()  # Stores the rank (pid) of the current process
stat = MPI.Status()

msg =  "Hello world, say process %s !" % rank

if rank == 0:
    # Master work
    print msg
    for i in range(num_procs - 1):
        msg = comm.recv(source=i+1, tag=MPI.ANY_TAG, status=stat)
        print (msg)

else:
    # Worker work
    comm.send(msg, dest = 0)


#Every time mpirun is executed, N_p processes are created,
# all with the same copy of the code.
# Single Program, Multiple Data (SPMD)

# They all start executing.

# The conditional statement that uses the rank of the process will
# determine the part of the code that each process runs.
# Everything outside the conditional statements is executed by all the processes.

# Each process is indepent from the other, except when communicating.

# The message tag is used to indicate the receiver the type of message received.
