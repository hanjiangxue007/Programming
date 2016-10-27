# Bhishan Poudel
# Sep 23, 2016

EXECS = hello
MPICC = mpifort

all: ${EXECS}
	mpirun -n 4 ./hello

mpi_hello_world: mpi_hello_world.f90
	${MPICC} -o hello hello.f90
    
    
clean:
	rm ${EXECS}
