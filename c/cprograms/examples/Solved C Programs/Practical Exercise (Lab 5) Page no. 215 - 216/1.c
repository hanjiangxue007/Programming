/*1.	Write a C program to calculate factorial of user inputed number by using function.*/
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
	int i;
	long int f;
	f=1;
	for(i=n;i>=1;i--)
	{
		f=f*i;
	}
	return(f);
}
