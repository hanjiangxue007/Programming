/*5.	Write a C program to add three numbers by using pointer.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int x,y,z,sum;
	int *a,*b,*c;
	printf("Enter the first number : ");
	scanf("%d",&x);
	printf("Enter the second number : ");
	scanf("%d",&y);
	printf("Enter the third number : ");
	scanf("%d",&z);
	a=&x;
	b=&y;
	c=&z;
	sum= *a + *b + *c;
	printf("\n the sum of the two numbers=%d", sum);
	getch();
}

