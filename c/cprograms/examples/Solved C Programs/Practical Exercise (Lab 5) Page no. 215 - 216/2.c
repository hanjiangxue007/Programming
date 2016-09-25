/*2.	What is recursive function? Write a program to calculate the factorial of an integer using recursion. (HSEB 2068)*/
#include<stdio.h>
#include<conio.h>
long int factorial(int);
main()
{
	int n;
	long int f;
	printf("\nEnter a number ");
	scanf("%d",&n);
	f=factorial(n);
	printf("\nthe factorial value=%ld",f);
	getch();
}
long int factorial(int n)
{
	
	long int f;
	if(n==0)
	{
		f=1;
	}
	else
	{
		f=n*factorial(n-1);
	}
	return(f);
}
