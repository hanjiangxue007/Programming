/*12.	Write a program to input an integer number and checks whether it is prime or not.*/
#include<stdio.h>
#include<conio.h>
main()
{
int n,r,i;
printf("\n Enter a number  ");
scanf("%d",&n);
for(i=2;i<n;i++)
{
if(n%i==0)
{
  printf("%d is not prime",n);
  break;
}
}
if(i==n)
printf("\n%d is prime",n);
getch();
}

