/*Write a C program to Swap (Exchange) two values of the variables without using third variables */
#include<stdio.h>
#include<conio.h>
main()
{
int a,b;
printf("\nEnter two values: ");
scanf("%d %d",&a,&b);
printf("\nBefore swapping a = %d and b = %d",a,b);
a = a^b;
b = b^a;
a = a^b;
printf("\nAfter swapping a = %d and b = %d",a,b);
getch();
}
