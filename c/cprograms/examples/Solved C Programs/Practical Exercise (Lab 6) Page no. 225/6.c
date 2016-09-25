/*6)	Write a program to input name of the months and monthly income and expenditure of an office during last year and
display the records properly. Also calculate the total and average income and expenditure of the office in last year. */
#include<stdio.h>
#include<conio.h>
main()
{
	struct office
	{
		char mname[20];
		float inc;
		float exp;
	};
	struct office off[12];
	float tinc,texp;
	int i;
	//code to input
	for(i=0;i<12;i++)
	{
		fflush(stdin);
		printf("\n Enter the name of the month ");
		gets(off[i].mname);
		printf("\nEnter the income amount of this month ");
		scanf("%f",&off[i].inc);
		printf("\nEnter the expenditure amount of this month ");
		scanf("%f",&off[i].exp);
	}
	//code to display
	printf("\nName of Month\tIncome\tExpenditure");
	for(i=0;i<12;i++)
	{
		printf("\n%d\t%s\t%s",off[i].mname,off[i].inc,off[i].exp);
	}
	//code to find total
	tinc=0;
	texp=0;
	for(i=0;i<12;i++)
	{
		tinc=tinc+off[i].inc;
		texp=texp+off[i].exp;
	}
	printf("\n\n\tTotal\tRs. %.2f\tRs. %.2f",tinc,texp);
	getch();
}
	
	
