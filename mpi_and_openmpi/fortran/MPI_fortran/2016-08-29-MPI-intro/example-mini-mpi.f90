  !! Short MPI example program
  !! date: 2016-08-26

PROGRAM minimpi
  IMPLICIT NONE
  ! need to include definitions of constants
  ! some implementations provide the better f90
  ! USE MPI but some do not support it
 
  INCLUDE 'mpif.h'

  ! FORTRAN implementation uses standard data types
  ! some will require predefine KIND/DIMENSION values (later)
  INTEGER ierr,npe,myid

  ! start MPI system (required in all MPI programs before any other
  !  library routine is called)
  !  argument ierr: error flag is often not checked
  !  my experience: MPI will anyway abort run when something goes wrong
  
  CALL MPI_INIT(ierr)

  ! now lets find out how many MPI tasks are running
  ! arguments: input: MPI_COMM_WORLD is group (communicator) of all tasks runnning
  !            output: npe is number of tasks
  !                    ierr is always there
  CALL MPI_COMM_SIZE(MPI_COMM_WORLD,npe,ierr)
  ! and which task we are here
  ! arguments: input: MPI_COMM_WORLD is group (communicator) of all tasks runnning
  !            output: npe is number of tasks
  !                    ierr is always there
  CALL MPI_COMM_RANK(MPI_COMM_WORLD,myid,ierr)   

  ! each task gets its own part of the code
  
  SELECT CASE(myid)
   CASE(0)
    WRITE(*,*) 'This is task zero working ...'
   CASE(1)
    WRITE(*,*) 'I am task 1 and will do something different'
   CASE DEFAULT
    WRITE(*,*) 'I am task ',myid,' and would like to know what I shall do'
  END SELECT
  
  ! finalize MPI (required at the end of the code to prevent
  !    other tasks to be stopped)

  CALL MPI_FINALIZE(ierr)
    
END PROGRAM minimpi
