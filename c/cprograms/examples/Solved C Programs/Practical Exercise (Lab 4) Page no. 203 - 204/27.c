/*27)	Write a program to input any two matrices of 3*4 size and find their sum.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int m1[3][4],m2[3][4],m3[3][4],r,c;
	printf("Enter the elements of the first matrix ");
	for(r=0;r<3;r++)
	{
		for(c=0;c<4;c++)
		{
			scanf("%d",&m1[r][c]);
		}
	}
	printf("Enter the elements of the second matrix ");
	for(r=0;r<3;r++)
	{
		for(c=0;c<4;c++)
		{
			scanf("%d",&m2[r][c]);
		}
	}
	printf("The first matrix  is ");
	printf("\n");
	for(r=0;r<3;r++)
	{
		for(c=0;c<4;c++)
		{
			printf("%d\t",m1[r][c]);
		}
		printf("\n");
	}
	printf("The second matrix  is ");
	printf("\n");
	for(r=0;r<3;r++)
	{
		for(c=0;c<4;c++)
		{
			printf("%d\t",m2[r][c]);
		}
		printf("\n");
	}
	//code to add matrices
	for(r=0;r<3;r++)
	{
		for(c=0;c<4;c++)
		{
			m3[r][c]=m1[r][c]+m2[r][c];
		}
	}
	printf("The sum of two matrices  is ");
	printf("\n");
	for(r=0;r<3;r++)
	{
		for(c=0;c<4;c++)
		{
			printf("%d\t",m3[r][c]);
		}
		printf("\n");
	}
	getch();
}