

program hello_world
    implicit none
    include 'mpif.h'
!    use mpi
    integer ierr, rank, comsize

    call MPI_INIT(ierr)
    call MPI_Comm_size(MPI_COMM_WORLD, comsize, ierr)
    call MPI_Comm_rank(MPI_COMM_WORLD, rank, ierr)
    print*, "Hello world, from ", rank, " of ", comsize


    call MPI_FINALIZE(ierr)
    stop
end
