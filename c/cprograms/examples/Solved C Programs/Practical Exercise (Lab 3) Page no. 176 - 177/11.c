/*11.	Write a C program to find a peculiar two digit number which is three times the sum of its digits.*/
#include<stdio.h>
#include<conio.h>
main()
{
int x,y,z=0, i;
for(i=10;i<=99;i++)
{
 x=i/10;
 y=i%10;
 z=3*(x+y);
if(i==z)
printf("\nThe peculiar two digit number is : %d\t",i);
}
getch();
}
