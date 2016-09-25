/*10.	Write a C program to print first 10 terms of the following series using FOR loop 1, 5, 9,  13   ………*/
#include<stdio.h>
#include<conio.h>
main()
{
int i, a=1;
printf("\nThe first 10 terms of the series is : ");
for(i=0;i<10;i++)
{
printf("%d, ",a);
a = a + 4;
}
getch();
}
