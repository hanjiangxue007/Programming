\\ Two digits

#include<stdio.h>
#include<conio.h>
main()
{
int i, s,f;
for(i=10;i<=99;i++)
{
s=i%10;
f=i/10;
if(((s-4)==f)&&(i%(f+s))==7)
printf("\n%d",i);
}
getch();
} 
