/*10.	Write a C program to print series 1, 4, 9, …  upto N by using function.*/
#include<stdio.h>
#include<conio.h>
void series(int);
main()
{
	int n;
	long int f;
	printf("\nEnter a number ");
	scanf("%d",&n);
	printf("\nThe required series is ");
	series(n);
	getch();
}
void series(int n)
{
	int i;
	for(i=1;i<=n;i=i+4)
	{
		printf("%d\t",i);
	}
}
