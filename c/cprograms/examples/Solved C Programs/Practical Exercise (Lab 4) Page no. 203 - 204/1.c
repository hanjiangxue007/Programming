/*1)	Write a program to input any 10 numbers in an array and find the total.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int num[10],i,t;
	printf("\nEnter any 10 numbers ");
	for(i=0;i<10;i++)
	{
		scanf("%d",&num[i]);
	}
	printf("\n The numbers are ");
	for(i=0;i<10;i++)
	{
		printf("%d ",num[i]);
	}
	t=0;
	for(i=0;i<10;i++)
	{
		t=t+num[i];
	}
	printf("\n The total=%d",t);
	getch();
}