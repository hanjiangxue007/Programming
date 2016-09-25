/*17)	Write a program to input any 50 numbers in an array and find the smallest number.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int num[50],i,smallest;
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
	//code to find smallest number
	smallest=num[0];
	for(i=0;i<50;i++)
	{
		if(num[i]<smallest)
		{
			smallest=num[i];
		}
	}
	printf("\n the smallest number=%d",smallest);
	getch();
}