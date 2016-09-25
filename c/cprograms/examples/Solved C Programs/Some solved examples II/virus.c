#include<stdio.h>
void f()
{
int j=11;
*(&j+2) += 14;
}
main()
{
int i;
i=15;
f();
i = 5;
i = -36;
printf ("\n%d\n",i);
getch();
}
