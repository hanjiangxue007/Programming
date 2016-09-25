/*4.	Write a program to find out whether it is an odd number or even number. (HSEB 2062,2068)*/
#include<stdio.h>
#include<conio.h>
main()
{
	int n,r;
	printf("\nEnter a number ");
	scanf("%d",&n);
	r=n%2;
	if(r==0)
	{
		printf("\n%d is even number",n);
	}
	else
	{
		printf("\n%d is odd number",n);
	}
	getch();
}
