/*6.	Write a C program to print Fibonacci series upto N terms. [Fibonacci series: 1, 1, 2, 3, 5, 8, 13, ……]*/
#include<stdio.h>
#include<conio.h>
main()
{
	int a,b,f,n,i;
	printf("Enter the value of 'n' th term : ");
	scanf("%d",&n);
	printf("\n The fibonacci series up to %d th term is :\n\n ",n);
	a = 0;
	b = 1;
	f = 1;
	for(i=1;i<=n;i++)
	{
		printf("%d\t",f);
		f = a + b;
		a=b;
		b=f;
	}
	getch();
}
