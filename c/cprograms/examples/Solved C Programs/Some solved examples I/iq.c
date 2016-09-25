/* Bacteria are known to multiply very rapidly. 
If a certain container contains just one bacterium on the first day
 and there are twice as many on the next day. In this manner the number
  of bacteria in the container doubles itself everyday. Assuming that the 
  container would be full on the 10th day with 13,312 bacteria, 
  find the number of bacteria that was initially in the container on the first day.
*/
#include<stdio.h>
#include<conio.h>
main()
{
 int x=13312,y;
 y=x/pow(2, 9);
 printf("\nThe total number of bacteria at first day is %d",y);
 getch();
}
