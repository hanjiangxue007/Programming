/*8.	Write a C program to read N numbers and calculate sum of even numbers and sum of odd numbers by using function.*/
#include<stdio.h>
#include<conio.h>
#define N 500
int sumofeven(int [],int);
int sumofodd(int [],int);
main()
{
	int i,num[N],sum1,sum2,n;
	printf("Enter the value of 'n'  ");
	scanf("%d",&n);
	printf("\nEnter any %d numbers ",n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&num[i]);
	}
	sum1=sumofeven(num,n);
	sum2=sumofodd(num,n);
	printf("\nThe sum of even numbers=%d",sum1);
	printf("\nthe sum of odd numbers=%d",sum2);
	getch();
}
int sumofeven(int x[N],int n)
{
	int i,s=0;
	for(i=0;i<n;i++)
	{
		if(x[i]%2==0)
		{
			s=s+x[i];
		}
	}
	return(s);
}
int sumofodd(int x[N],int n)
{
	int i,s=0;
	for(i=0;i<n;i++)
	{
		if(x[i]%2==1)
		{
			s=s+x[i];
		}
	}
	return(s);
}
