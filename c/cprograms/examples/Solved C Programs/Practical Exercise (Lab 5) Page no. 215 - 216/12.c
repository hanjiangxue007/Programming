/*12.	Write a C program to to calculate LCM of user inputed three numbers by using function.*/
#include<stdio.h>
#include<conio.h>
int LCM(int,int,int);
main()
{
	int n1,n2,n3,ans;
	printf("\nEnter first number ");
	scanf("%d",&n1);
	printf("\nEnter second number ");
	scanf("%d",&n2);
	printf("\nEnter third number ");
	scanf("%d",&n3);
	ans=LCM(n1,n2,n3);
	printf("\nthe LCM of given numbers=%d",ans);
	getch();
}
int LCM(int a,int b,int c)
{
	int i,r1,r2,r3,ans,x,smallest;
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
	x=a*b*c;
	for(i=x;i>=1;i--)
	{
		r1=i%a;
		r2=i%b;
		r3=i%c;
		if(r1==0&&r2==0&&r3==0)
		{
			ans=i;
		}
	}
	return(ans);
}
