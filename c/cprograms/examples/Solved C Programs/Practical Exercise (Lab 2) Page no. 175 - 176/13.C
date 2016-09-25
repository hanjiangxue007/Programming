/*13.	Write a program to read two numbers and find the bigger number by using function.*/
#include<stdio.h>
#include<conio.h>
int bigger(int,int);
main()
{
	int n1,n2,big;
	printf("Enter the first number ");
	scanf("%d",&n1);
	printf("Enter the second number ");
	scanf("%d",&n2);
	big=bigger(n1,n2);
	printf("\nthe bigger number=%d",big);
	getch();
	return(0);
}
int bigger(int a,int b)
{
	if(a>b)
	{
		return(a);
	}
	else
	{
		return(b);
	}
}
