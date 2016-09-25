/*4.	Write a C program to print the following series of cube numbers up to nth term. 1, 8, 27, …*/
#include<stdio.h>
#include<conio.h>
main()
{
	int n,i,c;
	printf("Enter the 'n' th term of the series ");
	scanf("%d",&n);
	printf("\nthe required series is ");
	for(i=1;i<=n;i++)
	{
		c=i*i*i;
		printf("%d\t",c);
	}
	getch();
	return(0);
}