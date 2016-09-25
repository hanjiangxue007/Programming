/*30)	Write a program to display the following menu and prompt the user to input his/her choice and do the task accordingly in 
two matrices of 2*2 size.
1.	Sum of the matrices
2.	Difference of the matrices
3.	Product of the matrices
4.	Quit
*/
#include<stdio.h>
#include<conio.h>
#include<process.h>
main()
{
	int m1[2][2],m2[2][2],m3[2][2],r,c,ch,s,i;
	printf("***********MENU ***********");
	printf("\n1.Sum of the matrices");
	printf("\n2.Difference of the matrices");
	printf("\n3.Product of the matrices");
	printf("\n4.Quit");
	printf("\n\nEnter your choice ");
	scanf("%d",&ch);
	switch(ch)
	{
		case 1:
			printf("Enter the elements of the first matrix ");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					scanf("%d",&m1[r][c]);
				}
			}
			printf("Enter the elements of the second matrix ");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					scanf("%d",&m2[r][c]);
				}
			}
			printf("The first matrix  is ");
			printf("\n");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					printf("%d\t",m1[r][c]);
				}
				printf("\n");
			}
			printf("The second matrix  is ");
			printf("\n");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					printf("%d\t",m2[r][c]);
				}
				printf("\n");
			}
			//code to find sum
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					m3[r][c]=m1[r][c]+m2[r][c];
				}
			}
			printf("The sum  of two matrices  is ");
			printf("\n");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					printf("%d\t",m3[r][c]);
				}
				printf("\n");
			}
			break;
	case 2:
			printf("Enter the elements of the first matrix ");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					scanf("%d",&m1[r][c]);
				}
			}
			printf("Enter the elements of the second matrix ");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					scanf("%d",&m2[r][c]);
				}
			}
			printf("The first matrix  is ");
			printf("\n");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					printf("%d\t",m1[r][c]);
				}
				printf("\n");
			}
			printf("The second matrix  is ");
			printf("\n");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					printf("%d\t",m2[r][c]);
				}
				printf("\n");
			}
			//code to find difference
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					m3[r][c]=m1[r][c]-m2[r][c];
				}
			}
			printf("The difference  of two matrices  is ");
			printf("\n");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					printf("%d\t",m3[r][c]);
				}
				printf("\n");
			}
			break;
	case 3:
			printf("Enter the elements of the first matrix ");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					scanf("%d",&m1[r][c]);
				}
			}
			printf("Enter the elements of the second matrix ");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					scanf("%d",&m2[r][c]);
				}
			}
			printf("The first matrix  is ");
			printf("\n");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					printf("%d\t",m1[r][c]);
				}
				printf("\n");
			}
			printf("The second matrix  is ");
			printf("\n");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					printf("%d\t",m2[r][c]);
				}
				printf("\n");
			}
			//code to find product
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					s=0;
					for(i=0;i<2;i++)
					{
						s=s+m1[r][i]*m2[i][c];
					}
					m3[r][c]=s;
				}
			}
			printf("The product  of two matrices  is ");
			printf("\n");
			for(r=0;r<2;r++)
			{
				for(c=0;c<2;c++)
				{
					printf("%d\t",m3[r][c]);
				}
				printf("\n");
			}
			break;
		case 4:
			exit(0);
		default:
			printf("\n your choice is invalid ");
			printf("\n Please, enter your choice between 1 to 4 ");
	}
	getch();
}
