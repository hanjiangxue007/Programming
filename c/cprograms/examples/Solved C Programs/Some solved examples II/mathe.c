#include<stdio.h>
#include<conio.h>
main()
{
int i, e,x,y,c;
for(i=32;i<=99;i++)
{
 e=i*i;
 x=e/100;
 y=e%100;
 c=x+y;
if(i==c)
printf("%d\t",i);
}
getch();
}

