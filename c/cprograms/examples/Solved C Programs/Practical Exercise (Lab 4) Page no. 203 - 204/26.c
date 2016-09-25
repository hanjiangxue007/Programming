/*26)	Write a program to input a 2*3 matrix and display it properly.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int m[2][3],r,c;
	printf("Enter the elements of the matrix ");
	for(r=0;r<2;r++)
	{
		for(c=0;c<3;c++)
		{
			scanf("%d",&m[r][c]);
		}
	}
	printf("The required matrix is ");
	printf("\n");
	for(r=0;r<2;r++)
	{
		for(c=0;c<3;c++)
		{
			printf("%d\t",m[r][c]);
		}
		printf("\n");
	}
	getch();
}