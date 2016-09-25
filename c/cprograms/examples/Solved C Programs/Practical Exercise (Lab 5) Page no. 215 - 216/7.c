/*7.	Write a C program to calculate sum of even numbers by using recursion.*/
#include<stdio.h>
#include<conio.h>
long int sumofeven(int);
main()
{
	int n;
	long int s;
	printf("\nEnter last number of the series ");
	scanf("%d",&n);
	s=sumofeven(n);
	printf("\nthe sum of even numbers upto %d  = %ld",n,s);
	getch();
}
long int sumofeven(int n)
{
	
	long int ans;
	int i;
	if(n%2==1)
	{
    n=n-1;
}
	if(n<=0)
	{
		ans=0;
	}
	else
	{
		ans=n+sumofeven(n-2);
	}
	return(ans);
}
