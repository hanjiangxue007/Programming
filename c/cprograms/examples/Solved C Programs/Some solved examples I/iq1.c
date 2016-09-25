/* 5) Consider the following number 45*45=2025; 20+25=45.
Write a program to generate number between 10 and 99 that satisfies the above property.
*/
#include<stdio.h>
#include<conio.h>
main()
{
int i, e,x,y,c;
printf("\nThe following two digits numbers satisfies the given condition");
for(i=10;i<=99;i++)
{
 e=i*i;
 x=e/100;
 y=e%100;
 c=x+y;
if(i==c)
printf("\n%d is one value because %d X %d = %d and %d + %02d = %d",i, i, i, i*i, x, y, x+y);
}
getch();
}
