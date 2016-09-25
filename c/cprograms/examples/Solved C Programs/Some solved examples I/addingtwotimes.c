/*Write a C program to add two times in hours, minutes and seconds. */
#include<stdio.h>
#include<conio.h>
main()
{
int h1, m1, s1, h2, m2, s2, h, m, s;
printf("\nEnter first time in hour minute and second : ");
scanf("%d %d %d",&h1,&m1,&s1);
printf("\nEnter second time in hour minute and second : ");
scanf("%d %d %d",&h2,&m2,&s2);
s = (s1 + s2)%60;
m = ((m1 + m2) + (s1 + s2)/60)%60;
h = h1 + h2 + ((m1 + m2)+ (s1 + s2)/60)/60;
printf("\nThe sum of %d hr, %d min, %d sec and %d hr, %d min, %d sec is %d hour, %d minutes and %d seconds",h1, m1, s1, h2, m2, s2, h, m, s);
getch();
}

