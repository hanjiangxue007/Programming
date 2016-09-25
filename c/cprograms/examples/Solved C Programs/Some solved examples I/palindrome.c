/*Write a C program to check user inputed number is palindrome or not.*/
#include<stdio.h>
#include<conio.h>
main()
{
int a,b,c,d;
printf("\nEnter any number to check palindrome or not : ");
scanf("%d",&a);
b=a;
d = 0;
while(a>0)
{
c=a%10;
d = d*10+c;
a = a/10;
}
if(d==b)
printf("\nThe number %d is palindrome",b);
else 
printf("\nThe number %d is not palindrome", b);
getch();
}
