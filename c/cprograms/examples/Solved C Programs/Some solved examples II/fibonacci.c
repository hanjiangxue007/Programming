/* Write a program to find Fibonacci series */

#include<stdio.h>
#include<conio.h>
main()
{
int n, i, a=1, b=0, f=1;
printf("\nHow many terms: ");
scanf("%d",&n);
for(i=1;i<n;i++)
{
printf("\t%d",f);
a=b;
b=f;
f=a+b;
}
getch();
} 
