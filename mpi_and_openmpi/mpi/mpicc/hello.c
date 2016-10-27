/* Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
 * Date        : Sep 01, 2016
 * Last update :
 *
 * Compile     : mpicc hello.c -o hello
 * Run         : mpirun -np 2 ./hello
 *
 *
 * Inputs      : 1.
 *
 *
 * Outputs     : 1.
 *
 * Info        :
 *
 * Ref: https://jetcracker.wordpress.com/2012/03/01/how-to-install-mpi-in-ubuntu/
 */


#include <mpi.h>
#include <stdio.h>
 
int main (int argc, char* argv[])
{
  int rank, size;
 
  MPI_Init (&argc, &argv);      /* starts MPI */
  MPI_Comm_rank (MPI_COMM_WORLD, &rank);        /* get current process id */
  MPI_Comm_size (MPI_COMM_WORLD, &size);        /* get number of processes */
  printf( "Hello world from process %d of %d\n", rank, size );
  MPI_Finalize();
  return 0;
}

