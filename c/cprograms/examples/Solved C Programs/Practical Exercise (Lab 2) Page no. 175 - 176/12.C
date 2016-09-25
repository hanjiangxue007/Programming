/*12.	Write a C program to print all Armstrong number form 1 to 1000*/
#include<stdio.h>
#include<conio.h>
main()
{
	int i,n,a,x,r;
	printf("\n the series of armstrong numbers upto 1000 are ");
	for(i=1;i<=1000;i++)
	{
		n=i;
		a=i;
		x=0;
		while(n>0)
		{
			r=n%10;
			x=x+r*r*r;
			n=n/10;
		}
		if(x==a)
		{
			printf("%d\t",a);
		}
	}
	getch();
}
