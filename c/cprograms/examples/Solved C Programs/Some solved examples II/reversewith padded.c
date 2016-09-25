\\ Reverse with padded

#include<stdio.h>
#include<conio.h>
main()
{
int i,r,n,x, c=0;
printf("Enter a number ");
scanf("%d",&n);
if(n>0)
{
x=0;
while(n>0)
{
r=n%10;
x=x*10+r;
n=n/10;
c++;
}
printf("\n the reverse number is =%0*d",c,x);
}   
else
{
printf("\nIt is not a positive number");
}
getch();
}
