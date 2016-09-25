/*1.	Write a C program to add two values by using pointer.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int x,y,sum;
	int *a,*b;
	printf("Enter the first number : ");
	scanf("%d",&x);
	printf("Enter the second number : ");
	scanf("%d",&y);
	a=&x;
	b=&y;
	sum= *a + *b;
	printf("\n the sum of the two numbers=%d", sum);
	getch();
}