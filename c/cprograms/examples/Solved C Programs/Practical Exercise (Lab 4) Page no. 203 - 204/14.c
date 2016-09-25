/*14)	Write a program to input any 50 numbers and count how many numbers are there which are exactly divisible by 7.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int num[50],i,c;
	printf("\nEnter  any 50 numbers ");
	for(i=0;i<50;i++)
	{
		scanf("%d",&num[i]);
	}
	printf("\n The numbers are ");
	for(i=0;i<50;i++)
	{
		printf("%d ",num[i]);
	}
	for(i=0;i<50;i++)
	{
		if(num[i]%7==0)
		{
			c++;
		}
	}
	printf("\n there are %d numbers which are exactly divisible by 7",c);
	getch();
}