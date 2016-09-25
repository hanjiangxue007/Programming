/* 13.	Write a C program to check whether user input number is prime or not?*/
#include<stdio.h>
#include<conio.h>
main()
{
int i, n;
printf("\nEnter any number : ");
scanf("%d",&n);
for(i=2;i<n;i++)
{
if(n%i==0)
{
printf("\nThe number %d is not prime",n);
break;
}
}
if(i==n)
printf("\nThe number %d is prime",n);
getch();
}
