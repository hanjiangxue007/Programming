/*9.	Write an algorithm to input a number and find whether it is exactly divisible by both 5 and 8 or not.  Convert the algorithm into C program code.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int n,r1,r2;
	printf("Enter a number ");
	scanf("%d",&n);
	r1=n%5;
	r2=n%8;
	if(r1==0&&r2==0)
	{
		printf("\n%d is exactly divisible by both 5 and 8",n);
	}
	else if(r1==0)
	{
		printf("\n%d is exactly divisible by  5 only but not by 8",n);
	}
	else if(r2==0)
	{
		printf("\n%d is exactly divisible by  8 only but not by 5",n);
	}
	else 
	{
		printf("\n%d is not  divisible by   5 and 8 both",n);
	}
	getch();
	return(0);
}