/*7.	Write an algorithm to input a number and print it is positive or negative number.  Then, Convert the algorithm into C program code.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int n,r;
	printf("Enter a number ");
	scanf("%d",&n);
	if(n>0)
	{
		printf("\n%d is positive number",n);
	}
	else
	{
		printf("\n%d is negative number",n);		
	}
	getch();
	return(0);
}