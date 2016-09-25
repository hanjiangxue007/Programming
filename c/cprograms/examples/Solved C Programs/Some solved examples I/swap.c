/*Write a C program to Swap (Exchange) two values of the variables */
#include<stdio.h>
#include<conio.h>
main()
{
int a, b, t;
printf("\nEnter two values: ");
scanf("%d %d", &a, &b);
printf("\nBefore swapping values of a = %d and b = %d", a,b);
t=a; //if a = 10 then a = 10, t=10.
a=b; //if b = 20 then a = 20, b=20.
b=t; // here b=10, t=10.
printf("\nAfter swapping values of a = %d and b = %d",a,b);
getch();
}
