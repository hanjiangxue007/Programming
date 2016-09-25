/*10.	Write a program to input any 3 numbers and find smallest number by using function.*/
#include<stdio.h>
#include<conio.h>
#include<process.h>
int smallest(int,int,int);
main()
{
	int n1,n2,n3,s;
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
	s=smallest(n1,n2,n3);
	printf("\nThe smallest number=%d",s);
	getch();
	return(0);
}
int smallest(int n1,int n2,int n3)
{
	int s;
	if(n1<n2 && n1<n3)
	{
		s=n1;
	}
	else if(n2<n1&& n2<n3)
	{
		s=n2;		
	}
	else
	{
		s=n3;
	}
	return(s);
}
