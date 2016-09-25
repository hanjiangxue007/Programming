/*14.	Write a C program to read two numbers sum them and display result by using pointer.*/
#include<stdio.h>
#include<conio.h>
main()
{
int a, b, *p, *q, sum = 0;
printf("\nEnter two numbers: ");
scanf("%d %d", &a,&b);
p = &a;
q = &b;
sum = *p + *q;
printf("\nThe sum is %d",sum);
getch();
}
