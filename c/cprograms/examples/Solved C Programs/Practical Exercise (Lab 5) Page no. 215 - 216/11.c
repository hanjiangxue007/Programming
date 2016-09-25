/*11.	Write a C program to calculate HCF / GCD of 3 user inputed numbers by using function.*/
#include<stdio.h>
#include<conio.h>
int HCF(int,int,int);
main()
{
	int n1,n2,n3,ans;
	printf("\nEnter first number ");
	scanf("%d",&n1);
	printf("\nEnter second number ");
	scanf("%d",&n2);
	printf("\nEnter third number ");
	scanf("%d",&n3);
	ans=HCF(n1,n2,n3);
	printf("\nthe HCF/GCD of given numbers=%d",ans);
	getch();
}
int HCF(int a,int b,int c)
{
	int i,r1,r2,r3,ans,smallest;
	if(a<b && a<c)
	{
		smallest=a;
	}
	else if(b<a&& b<c)
	{
		smallest=b;
	}
	else
	{
		smallest=c;
	}
	for(i=1;i<=smallest;i++)
	{
		r1=a%i;
		r2=b%i;
		r3=c%i;
		if(r1==0&&r2==0&&r3==0)
		{
			ans=i;
		}
	}
	return(ans);
}
