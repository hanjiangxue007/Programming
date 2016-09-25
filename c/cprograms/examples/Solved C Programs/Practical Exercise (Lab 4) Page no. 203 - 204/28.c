/*28)	Write a program to input any two matrices of 2*3 size and find their difference.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int m1[2][3],m2[2][3],m3[2][3],r,c;
	printf("Enter the elements of the first matrix ");
	for(r=0;r<2;r++)
	{
		for(c=0;c<3;c++)
		{
			scanf("%d",&m1[r][c]);
		}
	}
	printf("Enter the elements of the second matrix ");
	for(r=0;r<2;r++)
	{
		for(c=0;c<3;c++)
		{
			scanf("%d",&m2[r][c]);
		}
	}
	printf("The first matrix  is ");
	printf("\n");
	for(r=0;r<2;r++)
	{
		for(c=0;c<3;c++)
		{
			printf("%d\t",m1[r][c]);
		}
		printf("\n");
	}
	printf("The second matrix  is ");
	printf("\n");
	for(r=0;r<2;r++)
	{
		for(c=0;c<3;c++)
		{
			printf("%d\t",m2[r][c]);
		}
		printf("\n");
	}
	//code to find difference of the  matrices
	for(r=0;r<2;r++)
	{
		for(c=0;c<3;c++)
		{
			m3[r][c]=m1[r][c]-m2[r][c];
		}
	}
	printf("The difference of two matrices  is ");
	printf("\n");
	for(r=0;r<2;r++)
	{
		for(c=0;c<3;c++)
		{
			printf("%d\t",m3[r][c]);
		}
		printf("\n");
	}
	getch();
}