/*20)	Write a program to input any 10 numbers in an array and sort them in descending order.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int num[10],i,j,t;
	printf("\nEnter any 10 numbers ");
	for(i=0;i<10;i++)
	{
		scanf("%d",&num[i]);
	}
	printf("\n The numbers before sorting are ");
	for(i=0;i<10;i++)
	{
		printf("%d ",num[i]);
	}
	//code to sort
	for(i=0;i<10;i++)
	{
		for(j=0;j<9;j++)
		{
			if(num[j]<num[j+1])
			{
				t=num[j];
				num[j]=num[j+1];
				num[j+1]=t;
			}
		}
	}
	printf("\n The numbers after sorting are ");
	for(i=0;i<10;i++)
	{
		printf("%d ",num[i]);
	}
	getch();
}