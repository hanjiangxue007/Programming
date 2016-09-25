/* 11.	Write a program to read a four digit number and display it in reverse order.*/
#include<stdio.h>
#include<conio.h>
main()
{
int n, m, b, c, r = 0;
printf("\nEnter any three digit number : ");
scanf("%d", &n);
m = n;
b = n % 10; //extracting last number from 153 digit number i.e. 3
n = n / 10; //extracting number except last digit 3 i.e. 15
c = n % 10; // extracting last number from 15 i.e. 5
n = n / 10; //extracting number except last number 5 i.e. 1
r = b*100+c*10+n;
printf("\nThe reverse number of %d is %03d ", m, r);//%03 is used to padded zeros for making three digits.
getch();
}
