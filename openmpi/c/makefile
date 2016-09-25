# Bhishan Poudel
# Sep 23, 2016

EXECS = mpi_hello_world
MPICC = mpicc

all: ${EXECS}
	mpirun -n 4 ./mpi_hello_world

mpi_hello_world: mpi_hello_world.c
	${MPICC} -o mpi_hello_world mpi_hello_world.c
    
    
clean:
	rm ${EXECS}
