/*4.	Write a C program to pass out number of elements and sort them in ascending order by using function.*/
#include<stdio.h>
#include<conio.h>
#define N 1000
void sort(int[],int);
main()
{
	int num[N],n,i;
	printf("\nEnter the value of 'n' ");
	scanf("%d",&n);
	printf("\nEnter different number ");
	for(i=0;i<n;i++)
	{
		scanf("%d",&num[i]);
	}
	//code to call function
	sort(num,n);
	//display in ascending order
	printf("\nThe numbers in ascending order ");
	for(i=0;i<n;i++)
	{
		printf("  %d",num[i]);
	}
	getch();
}
void sort(int x[N],int n)
{
	int i,j,t;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-1;j++)
		{
			if(x[j]>x[j+1])
			{
				t=x[j];
				x[j]=x[j+1];
				x[j+1]=t;
			}
		}
	}
}
