  !! Short MPI example program
  !! date: 2016-08-26

PROGRAM summpi
  IMPLICIT NONE
  ! need to include definitions of constants
  ! some implementations provide the better f90
  ! USE MPI but some do not support it

  ! just to fix precision to at least 12 digits (double precision) 
  INTEGER,PARAMETER :: dpreal=SELECTED_REAL_KIND(12)

  INCLUDE 'mpif.h'

  ! FORTRAN implementation uses standard data types
  ! some will require predefine KIND/DIMENSION values (later)
  INTEGER ierr,npe,myid
  ! here we need variable for local result and for the complete result 
  REAL(dpreal) locres,res 

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

  ! we write only on one task to have nice outputs 
  IF(myid==0) THEN
    WRITE(*,*) 'Let us make sure that we use the right dpreal: ',dpreal
  END IF

  ! generate a local result, here the square of the id+1
  locres=(myid+1)**2

  ! collective reduce operation. all tasks of MPI_COMM_WORLD need to call
  ! this routine. It will only return when all tasks have reached this call.
  !   input:  locres buffer of count=1 double precision REALs
  !           collective operation: MPI_SUM (also: possible MPI_MAX,MPI_MIN,MPI_PROD, ...)
  !   output: res buffer of count=1 double precision REALs
  !           will be used only on root=0 task
  !   
  CALL MPI_REDUCE(locres,res,1,MPI_REAL8,MPI_SUM,0,MPI_COMM_WORLD,ierr)

  ! now print total result (only on root)

  IF(myid==0) THEN
   WRITE(*,*) 'The sum of all tasks is: ',res
  END IF
  
  ! finalize MPI (required at the end of the code to prevent
  !    other tasks to be stopped)

  CALL MPI_FINALIZE(ierr)
    
END PROGRAM summpi
