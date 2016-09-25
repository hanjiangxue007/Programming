!Author: Bhishan Poudel
!cmd   : clear; gfortran searchstring.f90 && ./a.out

program hello
implicit none

   character(len=30) :: myString
   character(len=10) :: testString
   
   myString   = 'This is a test'
   testString = 'test'
   
   if(index(myString, testString) == 0)then
      print *, 'test is not found'
   else
      print *, 'test is found at index: ', index(myString, testString)
   end if
   
end program hello
