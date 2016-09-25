/*21)	Write a program to input the marks of ‘n’ numbers of students and sort them in ascending order.*/
#include<stdio.h>
#include<conio.h>
#define N 1000
main()
{
	int num[N],i,j,t,n;
	printf("Enter the value of 'n' ");
	scanf("%d",&n);
	printf("\nEnter any n numbers ");
	for(i=0;i<n;i++)
	{
		scanf("%d",&num[i]);
	}
	printf("\n The numbers before sorting are ");
	for(i=0;i<n;i++)
	{
		printf("%d ",num[i]);
	}
	//code to sort
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-1;j++)
		{
			if(num[j]>num[j+1])
			{
				t=num[j];
				num[j]=num[j+1];
				num[j+1]=t;
			}
		}
	}
	printf("\n The numbers in ascending order are ");
	for(i=0;i<n;i++)
	{
		printf("%d ",num[i]);
	}
	getch();
}
