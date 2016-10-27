PROGRAM serial
IMPLICIT NONE
real integral, a, b, h, x
integer n, i 

real f
external f

print *, 'Enter a, b, and n' 
read*, a, b, n
h = (b-a)/n
integral = (f(a) + f(b))/2.0 
x=a
do i = 1 , n-1
    x=x+h
    integral = integral + f(x) 
enddo
integral = integral*h
print *,'With n =', n,' trapezoids, our estimate'
print *,'of the integral from ', a, ' to ',b, ' = ' , integral
end

real function f(x)
IMPLICIT NONE
real x
! Calculate f(x).
f = x*x 
return
end
