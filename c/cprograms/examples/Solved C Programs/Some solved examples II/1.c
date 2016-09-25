#include<stdio.h>
#include<string.h>
#include<conio.h>
main()
{
char a[] = "123456789", b[10];
strcpy(b,a);
strrev(b);
int i, c=10;
for(i=1;i<=5;i++)
{
printf("\n\t\t%10.*s",i,a);
printf("%-10.*s",(i-1),strrev(a));
}
getch();
}
