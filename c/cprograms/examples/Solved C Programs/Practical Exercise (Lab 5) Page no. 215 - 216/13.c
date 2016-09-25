/*13.	Write a C program to find area of right angle triangle whose height and base are input by user also using function.*/
#include<stdio.h>
#include<conio.h>
float areaoftriangle(float ,float);
main()
{
	float h,b,a;
	printf("\nEnter the height of triangle ");
	scanf("%f",&h);
	printf("\nEnter the base of triangle ");
	scanf("%f",&b);
	a=areaoftriangle(h,b);
	printf("\nthe area of triangle=%f",a);
	getch();
}
float areaoftriangle(float h,float b)
{
	float a;
	a=0.5*b*h;
	return (a);
}
