  subroutine gauss8(f,a,b,gaussint8)
!==========================================================
! Integration of f(x) on [a,b]
! Method: Gauss 8 points  
! written by: Alex Godunov (October 2009)
!----------------------------------------------------------
! IN:
! f   - subroutine to integrate (supplied by a user)
! a	  - Lower limit of integration
! b	  - Upper limit of integration
! OUT:
! gauss8 - Result of integration
!==========================================================
implicit none
integer, parameter :: n=4
double precision gaussint8, f, a, b
double precision ti(n), ci(n)
data ti/0.1834346424, 0.5255324099, 0.7966664774, 0.9602898564/
data ci/0.3626837833, 0.3137066458, 0.2223810344, 0.1012285362/ 
double precision r, m, c
integer i

r = 0.0;
m = (b-a)/2.0;
c = (b+a)/2.0;

do i = 1,n 
   r = r + ci(i)*(f(m*(-1.0)*ti(i) + c) + f(m*ti(i) + c))
end do
gaussint8 = r*m
return
end subroutine gauss8

  subroutine gauss16(f,a,b,gaussint16)
!==========================================================
! Integration of f(x) on [a,b]
! Method: Gauss 16 points  
! written by: Alex Godunov (October 2009)
!----------------------------------------------------------
! IN:
! f   - subroutine to integrate (supplied by a user)
! a	  - Lower limit of integration
! b	  - Upper limit of integration
! OUT:
! gauss8 - Result of integration
!==========================================================
implicit none
integer, parameter :: n=8
double precision gaussint16, f, a, b
double precision ti(n), ci(n)
data ti/0.0950125098, 0.2816035507, 0.4580167776, 0.6178762444, &  
        0.7554044083, 0.8656312023, 0.9445750230, 0.9894009349/ 
data ci/0.1894506104, 0.1826034150, 0.1691565193, 0.1495959888, &
        0.1246289712, 0.0951585116, 0.0622535239, 0.0271524594/ 
double precision r, m, c
integer i

r = 0.0;
m = (b-a)/2.0;
c = (b+a)/2.0;

do i = 1,n 
   r = r + ci(i)*(f(m*(-1.0)*ti(i) + c) + f(m*ti(i) + c))
end do
gaussint16 = r*m
return
end subroutine gauss16

