!Topic     : Assign1 Q2
!Programmer: Bhishan Poudel
!cmd       : clear; f90 -o modexample modexample.f90 && ./modexample

program modexample
implicit none

      integer x, i
      
      

      do i=-4,4,1
          if(mod(i,3) ==0) then     
              x = 2*i

              write (*,100) i,x
          end if

      end do
      
      100 format(1x,T2,i4,T8,i4)  ! formatting for 1 integer and 9 float points
     
      
   
end program modexample

