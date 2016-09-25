/*8.	Write a C program to find the GCD of 4 integers.*/
#include<stdio.h>
#include<conio.h>
main()
{
int i, a, b, c, d;
printf("\nEnter any four numbers : ");
scanf("%d %d %d %d", &a, &b, &c, &d);
for(i=a;i>0;i--)
{
if(a%i == 0 && b % i == 0 && c % i == 0 && d % i == 0)
{
printf("\nThe GCD of %d %d %d and %d is %d", a, b, c, d, i);
break;
}
}
getch();
}
