/*12)	Write a program to input any 50 numbers in an array and count how many are even and odd numbers are in the list.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int num[50],i,c1,c2;
	float avg;
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
	c1=c2=0;
	for(i=0;i<50;i++)
	{
		if(num[i]%2==0)
		{
			c1++;
		}
		else
		{
			c2++;
		}
	}
	printf("\n The no. of even numbers =%d",c1);
	printf("\n the no. of odd numbers=%d",c2);
	getch();
}