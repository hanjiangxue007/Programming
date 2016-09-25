/*Wrie a recursive C program to calculate factorial user inputed number  */
#include<stdio.h>
#include<conio.h>
int fact(int);
main()
{
int f, n;
printf("\nEnter any number: ");
scanf("%d",&n);
f=fact(n);
printf("\nThe factorial of %d is %d",n,f);
getch();
}
fact(int p)
{
if(p==0)
return(1);
else if(p==1)
return(1);
else
return(p*fact(p-1));
}
