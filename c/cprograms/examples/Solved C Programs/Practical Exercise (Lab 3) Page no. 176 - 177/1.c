/*1.	Write a C program to read any number and display 1 for January, 2 for February ……….., 12 for December and other for 'wrong input'.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int a;
	printf("\nEnter a number between 1 to 12 ");
	scanf("%d",&a);
	switch(a)
	{
		case 1:
			printf("\nJanuary");
			break;
		case 2:
			printf("\nFebruary");
			break;
		case 3:
			printf("\nMarch");
			break;			
		case 4:
			printf("\nApril");
			break;
		case 5:
			printf("\nMay");
			break;
		case 6:
			printf("\nJune");
			break;
		case 7:
			printf("\nJuly");
			break;
		case 8:
			printf("\nAugust");
			break;
		case 9:
			printf("\nSemptember");
			break;
		case 10:
			printf("\nOctober");
			break;
		case 11:
			printf("\nNovember");
			break;
		case 12:
			printf("\nDecember");
			break;
		default:
			printf("\n\nyou entered invalid number. Please enter a number between 1 to 12 ");
	}
	getch();
}