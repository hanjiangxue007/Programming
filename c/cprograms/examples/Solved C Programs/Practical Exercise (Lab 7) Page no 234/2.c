/*2.	Write a C program to show pointer arithmentic.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int a=10,*p1;
	float b=10.5,*p2;
	char c='A',*p3;
	
	printf("\nThe value of a=%d",a);
	printf("\n the value of b=%f",b);
	printf("\n the value of c=%c",c);
	p1=&a;
	p2=&b;
	p3=&c;
	printf("\n The memory address of p1 before increment=%u",p1);
	printf("\n The memory address of p2 before increment=%u",p2);
	printf("\n The memory address of p2 before increment=%u",p3);
	p1++;
	p2++;
	p3++;
	printf("\n************************");
	printf("\n The memory address of p1 after increment=%u",p1);
	printf("\n The memory address of p2 after increment=%u",p2);
	printf("\n The memory address of p2 after increment=%u",p3);
	getch();
	return(0);
}
