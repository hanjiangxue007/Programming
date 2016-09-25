/* 7.	Write a C program to calculate simple interest and compound interest.*/
#include<stdio.h>
#include<math.h>
#include<conio.h>
main()
{
float p,t,r,si,ci;
printf("\nEnter principal: ");
scanf("%f",&p);
printf("\nEnter time: ");
scanf("%f",&t);
printf("\nEnter rate of interest: ");
scanf("%f",&r);
si = p*t*r/100;
ci = p*(pow(1+r/100,t)-1);
printf("\nSimple interest is %.2f",si);
printf("\nCompound interest is %.2f",ci);
getch();
}
