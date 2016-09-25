/*3.	Write a program to input any three different numbers and find the middle value.*/
#include<stdio.h>
#include<conio.h>
#include<process.h>
main()
{
	int n1,n2,n3;
	printf("Enter first  number ");
	scanf("%d",&n1);
	printf("Enter second  number ");
	scanf("%d",&n2);
	printf("Enter third  number ");
	scanf("%d",&n3);
	if(n1==n2 || n1==n3||n2==n3)
	{
		printf("\nPlease, enter the different numbers ");
		getch();
		//exit(0);
	}
	if((n1>n2 && n1<n3)||(n1<n2&&n1>n3))
	{
		printf("\n%d is middle  number",n1);
	}
	else if((n2>n1&& n2<n3)||(n2<n1&&n2>n3))
	{
		printf("\n%d is middle number",n2);		
	}
	else
	{
		printf("\n%d is middle number",n3);
	}
	getch();
	return(0);
}
