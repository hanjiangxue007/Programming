//sprintf5.c
//cmd: clear; gcc sprintf5.c && ./a.out

#include <stdio.h>

   int main()
   {
      char b[100];
      int i = 42;
      float f = 1.1234f;
      sprintf( b, "Formatted data:  %d / %f", i, f );
      puts( b );
   }
