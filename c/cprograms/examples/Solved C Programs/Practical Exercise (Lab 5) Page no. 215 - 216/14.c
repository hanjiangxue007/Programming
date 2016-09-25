/*14.	Write a C program to find area of triangle whose 3 sides are input by user. [Hint: area = sqrt(s*(s-a)(s-b)(s-c)), 
where s = (a+b+c)/2 ]*/
#include<stdio.h>
#include<conio.h>
#include<math.h>
float areaoftriangle(float ,float,float);
main()
{
	float side1,side2,side3,a;
	printf("\nEnter the length of the first side of triangle ");
	scanf("%f",&side1);
	printf("\nEnter the length of the second side of triangle ");
	scanf("%f",&side2);
	printf("\nEnter the length of the third side of triangle ");
	scanf("%f",&side3);
	a=areaoftriangle(side1,side2,side3);
	printf("\nthe area of triangle=%f",a);
	getch();
}
float areaoftriangle(float a,float b,float c)
{
	float s,ar;
	s=(a+b+c)/2;
	ar=sqrt(s*(s-a)*(s-b)*(s-c));
	return (ar);
}
