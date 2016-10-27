program trapezoidal
implicit none
include 'mpif.h'

integer my_rank ! My process rank. 
integer p       ! The number of processes.

real a, b, h, local_a, local_b, integral, total
integer n, local_n, source, dest, tag
integer status(MPI_STATUS_SIZE), ierr
real trap
data a, b, n, dest, tag /0.0, 1.0, 1024, 0, 50/
! let the system do what it needs to start up MPI
call MPI_INIT(ierr)
! get my process rank
call MPI_COMM_RANK(MPI_COMM_WORLD, my_rank, ierr)
! find out how many processer are being used.
call MPI_COMM_SIZE(MPI_COMM_WORLD, p, ierr)
print*, "my_rank, p: ", my_rank, p

h = (b-a)/n
local_n = n/p

! length of each process 'interval of integration=local_n*h.
! so my interval status at:
local_a = a+my_rank*local_n*h
local_b = local_a + local_n*h
integral = Trap(local_a, local_b, local_n, h)

! add up the integrals calculated by each process.
if (my_rank .EQ. 0) then
    total = integral
    do source = 1, p-1
        call MPI_recv(integral, 1, MPI_real, source, tag, MPI_comm_world, status, ierr)
        total = total + integral
    enddo
else
    call MPI_send(integral, 1, MPI_real, dest, tag, MPI_comm_world, ierr)
endif

if (my_rank .EQ. 0) then
    write(6, 200) n
200 format(' ','With n = ',I4,' trapezoids, our estimate')
    write(6,300) a, b, total
300 format(' ','of the integral from ',f6.2,' to ',f6.2, ' = ', f11.5)
endif

! shut down MPI.

call MPI_finalize(ierr)
end program trapezoidal

real function Trap(local_a, local_b, local_n, h)
    implicit none
    integer local_n, i
    real local_a, local_b, h
    real integral, x
    real f
    
    integral = (f(local_a)+f(local_b))/2.0
    x = local_a
    do i = 1, local_n-1
        x = x+h
        integral = integral+f(x)
    enddo
    integral = integral*h
    Trap = integral
    return
    end


real function f(x) 
IMPLICIT NONE
real x
f = x*x 
return
end
