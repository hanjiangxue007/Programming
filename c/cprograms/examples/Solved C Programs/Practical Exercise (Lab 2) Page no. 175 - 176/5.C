/*5.	Write a C program to print multiplication table up to N.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int n,i,j,m;
	printf("Enter the last number for the series of multiplication table  ");
	scanf("%d",&n);
	 
	for(i=1;i<=n;i++)
	{
		printf("\nThe multiplication table of %d is ");
		printf("\n\n");
		for(j=1;j<=10;j++)
		{
			m=j*i;
			printf("\n%d * %d =%d",i,j,m);
		}
	}
	getch();
	return(0);
}