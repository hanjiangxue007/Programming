/*7)	Write a program to input any 50 numbers in an array and find the sum of odd numbers only.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int num[50],i,t;
	printf("\nEnter any 50 numbers ");
	for(i=0;i<50;i++)
	{
		scanf("%d",&num[i]);
	}
	printf("\n The numbers are ");
	for(i=0;i<50;i++)
	{
		printf("%d ",num[i]);
	}
	t=0;
	for(i=0;i<50;i++)
	{
		if(num[i]%2==1)
		{
			t=t+num[i];
		}
	}
	printf("\n The sum of odd numbers only=%d",t);
	getch();
}