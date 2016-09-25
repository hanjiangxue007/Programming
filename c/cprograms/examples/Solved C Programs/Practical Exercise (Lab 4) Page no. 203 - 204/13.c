/*13)	Write a program to input any 50 numbers and count how many are prime numbers.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int num[50],i,j,c,r,result=1;
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
		result=1;
		for(j=2;j<num[i];j++)
		{
			r=num[i]%j;
			if(r==0)
			{
				result=0;
				break;
			}
		}
		if(result==0)
		{
			continue;
		}
		else
		{
			c++;
		}
	}
	printf("\n the no. of prime numbers in the array=%d",c);
	getch();
}