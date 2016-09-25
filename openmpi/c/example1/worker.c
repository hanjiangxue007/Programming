/* Author      : Bhishan Poudel; Physics PhD Student, Ohio University
 * Date        : Sep 23, 2016
 * Last update :
 *
 * Compile     : gcc -Wall -O3 -o a a.c -lm -lcfitsio -lpthread -lfftw3f
 * Run         :
 *
 *
 * Info :
 *
 */

int main (int argc, char* argv[]){

  const int max_msg_length = 100;
  char message[max_msg_length+1];
  MPI_Status status ;
  int rank, num_procs ;
  int tag ;
  int mpi_error ;

  mpi_error = MPI_Init(&argc, &argv);
  mpi_error = MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  mpi_error = MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

  sprintf(message, "Hello world, say process #%d!", rank);

  // Master worker code in next slide
if(rank == 0){
    printf(message) ;
    for(int i = 0; i < num_procs-1; i++){
        mpi_error = MPI_Recv(message, max_msg_length + 1,
        MPI_CHAR, MPI_ANY_SOURCE, tag, MPI_COMM_WORLD,
            &status);
        printf(message) ;
    }
  }
  else{
    mpi_error_code = MPI_Send(message, strlen(message) + 1, MPI_CHAR,
        0, tag, MPI_COMM_WORLD);
  }

  mpi_error = MPI_Finalize();
  return 0;
}
