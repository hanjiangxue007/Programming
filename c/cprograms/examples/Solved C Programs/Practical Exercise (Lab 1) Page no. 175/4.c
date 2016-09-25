/*4.	Write a C program to add two distances in feet and inches.*/
#include<stdio.h>
#include<conio.h>
main()
{
int f1, i1, f2, i2, f, i;
printf("\nEnter first distance in feet and inches : ");
scanf("%d %d", &f1, &i1);
printf("\nEnter second distance in feet and inches : ");
scanf("%d %d", &f2, &i2);
i=(i1+i2)%12;
f=f1+f2 +(i1+i2)/12;
printf("\nSum of the two distances %d ft %d in and %d ft %d in is %d feet and %d inches", f1,i1,f2,i2,f,i);
getch();
}
