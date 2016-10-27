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
    print (msg)
    for i in range(num_procs - 1):
        msg = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=stat)
        print (msg)

else:
    # Worker work
    comm.send(msg, dest = 0)








#The main object is MPI

# MPI has two important members

# MPI.COMM_WORLD
# Defines the default communicator, which contains all processes.
# An MPI communicator is a collection of processes that can send messages to each other.
# MPI.Status()
# To keep track of the status of a communication.
# It has information on errors, source of communication, and others.





##==============================================================================
## Important routines
##==============================================================================
# Get_size()
# Returns the number of processes, N_p in a run.
# Get_rank()
# Returns the process ID of the current process.
# The process ID is a number between 0 and N_p - 1.
# send()
# Sends a message from the current process to some other destination process.
# recv()
# Receives a message on the current process from some source process.
# bcast()
# Broadcasts a message from one process to all others. I.E.
# One process sends and all others receives a message.
# reduce()
# Performs a reduction computation (i.e. SUM, PROD, MAX) of a variable on
# all processes, and the result is sent to a single process.

# Why mpi4py?

# Python
# Do I need to say more?
# Allows the use of python's efficient high-level data structures and
# approach to object-oriented programming with dynamic typing and dynamic binding.

# Permits the transmittion of any pickable python object
# lists, hashes, tuples, etc.
# mpi4py can be used for the processes communication and the heavy
# computational part can be implemented in C
