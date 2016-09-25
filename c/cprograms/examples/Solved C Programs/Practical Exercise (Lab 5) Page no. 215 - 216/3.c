/*3.	Write a C program to calculate factorial upto user input number by using function.*/
#include<stdio.h>
#include<conio.h>
long int factorial(int);
main()
{
	int n,i;
	long int f;
	printf("\nEnter a number ");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		f=factorial(i);
		printf("\nthe factorial value of %d =%ld",i,f);
	}
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
