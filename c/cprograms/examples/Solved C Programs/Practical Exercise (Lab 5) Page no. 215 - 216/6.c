/*6.	Write a C program to compound interest by using function.*/
#include<stdio.h>
#include<conio.h>
float compoundinterest(float,float,float);
main()
{
	float p,t,r,ci;
	printf("\nEnter the principle amount ");
	scanf("%f",&p);
	printf("\nEnter the time ");
	scanf("%f",&t);
	printf("\nEnter the rate of interest ");
	scanf("%f",&r); 
	ci=compoundinterest(p,t,r);
	printf("\nThe compound interest=Rs. %.2f",ci);
	getch();
}
float compoundinterest(float p,float t,float r)
{
	float amt;
	
	
	return(amt);
}
