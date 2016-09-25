/*3.	Write a C program to print all Armstrong numbers upto 1000.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int a,n,r,x;
	printf("The Armstrong number upto 1000 are ");
	for(a=1;a<=1000;a++)
	{
		n=a;
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
