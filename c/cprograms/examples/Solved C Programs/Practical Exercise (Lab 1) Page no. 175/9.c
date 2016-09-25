/* 9.	Write a C program to read a number and display it equivalence in octal and hexadecimal number.*/
#include<stdio.h>
#include<conio.h>
main()
{
int n, o, h;
printf("\nEnter any decimal number : ");
scanf("%d", &n);
printf("\nOctal of %d is %o", n,n);
printf("\nHexadecimal of %d is %X",n,n);
getch();
}
