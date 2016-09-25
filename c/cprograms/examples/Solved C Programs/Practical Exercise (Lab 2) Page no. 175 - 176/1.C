/*1.	For any integer input through the keyboard, write a C program to find out whether it is an odd number or even number.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int n,r;
	printf("Enter a number ");
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
	return(0);
}