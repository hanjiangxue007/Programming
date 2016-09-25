/*Write a C program to calculate Simple Interest. */
#include<stdio.h>
#include<conio.h>
main()
{
float p, t, r, si;
printf("\nEnter P, T and R: ");
scanf("%f %f %f", &p, &t, &r);
si = p*t*r/100;
printf("\nThe simple interest is %.2f",si);
getch();
}
