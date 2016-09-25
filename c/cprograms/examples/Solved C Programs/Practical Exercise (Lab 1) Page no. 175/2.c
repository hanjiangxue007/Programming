/*2.	Write a C program to convert days into year, months and remaining days.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int days, y, m, rd;
	printf("\nEnter the number of days:  ");
	scanf("%d",&days);
	y = days / 365;
	rd = days %365;
	m = rd / 30;
	rd = rd % 30;
	printf("\nThe %d days converted into %d year %d months and %d remaining days",days, y, m, rd);
	getch();
}
