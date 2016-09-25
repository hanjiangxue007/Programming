/*11.	Write an algorithm and C program to read a number and find is it exactly divisible by 3 and 5 or not?*/
#include<stdio.h>
#include<conio.h>
main()
{
	int n,r1,r2;
	printf("Enter a number ");
	scanf("%d",&n);
	r1=n%3;
	r2=n%5;
	if(r1==0&&r2==0)
	{
		printf("\n%d is exactly divisible by both 3 and 5",n);
	}
	else if(r1==0)
	{
		printf("\n%d is exactly divisible by  3 only but not by 5",n);
	}
	else if(r2==0)
	{
		printf("\n%d is exactly divisible by  5 only but not by 3",n);
	}
	else 
	{
		printf("\n%d is not  divisible by   3 and  5 both",n);
	}
	getch();
	return(0);
}