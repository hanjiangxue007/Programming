/* 10.	Write a C program to read a number and check it is Armstrong number or not. [Armstrong number 153 = 13+53+33]*/
#include<stdio.h>
#include<conio.h>
main()
{
int n, m, b, c, a = 0;
printf("\nEnter any three digit number : ");
scanf("%d", &n);
m = n;
b = n % 10; //extracting last number from 153 digit number i.e. 3
n = n / 10; //extracting number except last digit 3 i.e. 15
c = n % 10; // extracting last number from 15 i.e. 5
n = n / 10; //extracting number except last number 5 i.e. 1
a = b*b*b +c*c*c + n*n*n;
if(a == m)
printf("\nThe number %d is Armstrong number",m);
else 
printf("\n The number %d is not Armstrong number",m);
getch();
}
