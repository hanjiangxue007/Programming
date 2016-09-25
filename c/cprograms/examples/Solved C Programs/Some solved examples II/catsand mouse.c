#include<stdio.h>
#include<conio.h>
main()
{
int mice=999919,cats;
for(cats=2;cats<=999919;cats++)
{
 if(mice%cats==0)
 {
 printf("%d\n",cats);
}
}
getch();
}
