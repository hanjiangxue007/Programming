/*15)	Write a program to input any 50 numbers and count how many numbers are square and cube numbers.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int num[50],i,j,ans,result,c1,c2;
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
	//code to count square numbers
	for(i=0;i<50;i++)
	{
		result=0;
		for(j=1;j<=num[i];j++)
		{
			ans=j*j;
			if(ans==num[i])
			{
				result=1;
				break;
			}
		}
		if(result==1)
		{
			c1++;
		}
	}
	//code to count dube numbers
	for(i=0;i<50;i++)
	{
		result=0;
		for(j=1;j<=num[i];j++)
		{
			ans=j*j*j;
			if(ans==num[i])
			{
				result=1;
				break;
			}
		}
		if(result==1)
		{
			c2++;
		}
	}
	printf("\n the no. of square numbers in the array=%d",c1);
	printf("\n the no. of cube numbers in the array=%d",c2);
	getch();
}