/*9.	Write a recursive C program to calculate sum of odd numbers upto N.*/
#include<stdio.h>
#include<conio.h>
long int sumofodd(int);
main()
{
	int n;
	long int s;
	printf("\nEnter last number of the series ");
	scanf("%d",&n);
	s=sumofodd(n);
	printf("\nthe sum of even numbers upto %d  = %ld",n,s);
	getch();
}
long int sumofodd(int n)
{
	
	long int ans;
	int i;
	if(n%2==0)
	{
              n=n-1;
}
	if(n<=0)
	{
		ans=0;
	}
	else
	{
		ans=n+sumofodd(n-2);
	}
	return(ans);
}
