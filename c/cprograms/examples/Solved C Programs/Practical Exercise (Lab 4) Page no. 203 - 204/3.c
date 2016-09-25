/*3)	Write a program to input the monthly profit of a bank in a year and find the total and monthly average profit of the bank in that year.*/
#include<stdio.h>
#include<conio.h>
main()
{
	float profit[12],t,avg;
	int i;
	printf("\nEnter the monthly profit of a bank in a year  ");
	for(i=0;i<12;i++)
	{
		scanf("%f",&profit[i]);
	}
	printf("\n The monthly profit amount ");
	for(i=0;i<12;i++)
	{
		printf("%f ",profit[i]);
	}
	t=0;
	for(i=0;i<12;i++)
	{
		t=t+profit[i];
	}
	avg=t/12;
	printf("\n The average profit of a bank in a year=%f",avg);
	getch();
}