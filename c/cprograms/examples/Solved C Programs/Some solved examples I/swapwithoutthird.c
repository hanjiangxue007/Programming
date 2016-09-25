/*Write a C program to Swap (Exchange) two values of the variables without using third variables */
#include<stdio.h>
#include<conio.h>
main()
{
int a,b;
printf("\nEnter two numbers : ");
scanf("%d %d", &a, &b);
printf("\nThe value before swapping is a = %d and b = %d", a,b);
a = a+b; //if a = 10 and b = 20 then a = 30 at last.
b = a-b; //here b = 30-20 = 10.
a = a-b; //here a = 30-10 = 20.
printf("\nThe value of a = %d and b = %d", a,b);
getch();
}
