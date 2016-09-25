/*16)	Write a program to input any 50 numbers in an array and find the biggest number.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int num[50],i,biggest;
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
	//code to find biggest number
	biggest=num[0];
	for(i=0;i<50;i++)
	{
		if(num[i]>biggest)
		{
			biggest=num[i];
		}
	}
	printf("\n the biggest number=%d",biggest);
	getch();
}