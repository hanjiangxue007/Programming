\\ Type casting 

#include<stdio.h>
#include<conio.h>
main()
{
int p,t,r,i;
printf("\nEnter principal, time and rate:");
scanf("%d %d %d",&p, &t, &r);
i=p*t*r/100.00;
printf("%d",i);
getch();
}
