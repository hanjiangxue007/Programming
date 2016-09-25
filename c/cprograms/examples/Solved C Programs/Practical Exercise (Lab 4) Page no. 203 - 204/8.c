/*8)	Write a program to input any 10 numbers and count how many numbers are positive.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int num[10],i,c;
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
	c=0;
	for(i=0;i<10;i++)
	{
		if(num[i]>0)
		{
			c++;
		}
	}
	printf("\n The no. of positive numbers =%d",c);
	getch();
}