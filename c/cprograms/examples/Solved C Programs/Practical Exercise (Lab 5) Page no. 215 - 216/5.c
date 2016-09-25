/*5.	Write a C program to check user input number is even or odd by using function.*/
#include<stdio.h>
#include<conio.h>
int evenodd(int);
main()
{
	int n,ans;
	printf("\nEnter a number ");
	scanf("%d",&n);
	ans=evenodd(n);
	if(ans==0)
	{
		printf("\n%d is even number",n);
	}
	else
	{
		printf("\n%d is odd number",n);
	}
	getch();
}
int evenodd(int n)
{
	int r;
	r=n%2;
	if(r==0)
	{
		return (0);
	}
	else
	{
		return(1);
	}
}
