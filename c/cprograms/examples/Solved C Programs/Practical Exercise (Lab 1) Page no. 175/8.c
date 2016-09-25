/* 8.	WAP to read a 5 digit number and find sum of individual digits. i.e. 54879=5+4+8+7+9=33.*/
#include<stdio.h>
#include<conio.h>
main()
{
int i, n, m, a,b,c,d, s=0;
printf("\nEnter any 5 digit number (or UPTO 5 digits): ");
scanf("%d", &n);
m = n;
a = n % 10; //extract last number of 54879 i.e. 9
n = n / 10; //extract number except last number 9 i.e. 5487
b = n % 10; // extract last number of 5487 i.e. 7
n = n / 10; //extract number except last number 7 i.e. 548
c = n % 10; // extract last number of 548 i.e. 8
n = n / 10; //extract number except last number 8 i.e. 54
d = n % 10; //extract last number of 54 i.e. 4
n = n / 10; //extract number except last number 4 i.e. 5
s = a+b+c+d+n;
printf("\nThe sum of digits of %d is %d",m,s);
getch();
}
