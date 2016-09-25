/*29)	Write a program to input any two matrices of 3*3 sizes and find their product.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int m1[3][3],m2[3][3],m3[3][3],r,c,i,s;
	printf("Enter the elements of the first matrix ");
	for(r=0;r<3;r++)
	{
		for(c=0;c<3;c++)
		{
			scanf("%d",&m1[r][c]);
		}
	}
	printf("Enter the elements of the second matrix ");
	for(r=0;r<3;r++)
	{
		for(c=0;c<3;c++)
		{
			scanf("%d",&m2[r][c]);
		}
	}
	printf("The first matrix  is ");
	printf("\n");
	for(r=0;r<3;r++)
	{
		for(c=0;c<3;c++)
		{
			printf("%d\t",m1[r][c]);
		}
		printf("\n");
	}
	printf("The second matrix  is ");
	printf("\n");
	for(r=0;r<3;r++)
	{
		for(c=0;c<3;c++)
		{
			printf("%d\t",m2[r][c]);
		}
		printf("\n");
	}
	//code to multply matrices
	for(r=0;r<3;r++)
	{
		for(c=0;c<3;c++)
		{
			s=0;
			for(i=0;i<3;i++)
			{
				s=s+m1[r][i]*m2[i][c];
			}
			m3[r][c]=s;
      }
	}
	printf("The product of two matrices  is ");
	printf("\n");
	for(r=0;r<3;r++)
	{
		for(c=0;c<3;c++)
		{
			printf("%d\t",m3[r][c]);
		}
		printf("\n");
	}
	getch();
}
