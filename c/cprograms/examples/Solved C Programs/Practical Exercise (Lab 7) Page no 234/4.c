/*4.	Write a C program to pass a value to a function and check it is even or odd by using pointer parameter.*/
#include<stdio.h>
#include<conio.h>
char *EvenOdd(int );
main()
{
	int n;
	char *a;
	printf("Enter a number ");
	scanf("%d",&n);
	a=EvenOdd(n);
	printf("\n%s",a);
	getch();
}
char *EvenOdd(int n)
{
	int r;
	char *result;
	r=n%2;
	if(r==0)
	{
		result="It is even number";
	}
	else
	{
		result="It is odd number";
	}
	return(result);
}
	
