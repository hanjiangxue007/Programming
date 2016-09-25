/*25)	Write a program to store the following matrix and display it properly.
4	8	-2
3	4	0
*/
#include<stdio.h>
#include<conio.h>
main()
{
	int m[2][3]={{4,8,-2},{3,4,0}};
	int r,c;
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