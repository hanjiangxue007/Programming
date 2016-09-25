/*1.	Write a C program to read number of items, rate and calculate total amount.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int noi;
	float r,ta;
	printf("\nEnter the number of items:  ");
	scanf("%d",&noi);
	printf("\nEnter the rate of an item:  ");
	scanf("%f",&r);
	ta=noi*r;
	printf("\nThe total amount =Rs. %f",ta);
	getch();
}