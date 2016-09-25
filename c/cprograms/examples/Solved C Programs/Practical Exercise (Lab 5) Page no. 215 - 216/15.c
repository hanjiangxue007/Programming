/*15.	Write a C program to read two equation ax2+bx+c = 0 and dx2+ex+f=0 and sum them by using function.*/
#include<stdio.h>
#include<conio.h>
void equation_adder(int, int, int, int, int, int);
main()
{
int a,b,c,d,e,f;
printf("\nEnter values of a, b, c for first equation ax^2+bx+c=0 : ");
scanf("%d %d %d", &a, &b, &c);
printf("\nEnter values of d, e, f for second equation dx^2+ex+f=0 : ");
scanf("%d %d %d", &d, &e, &f);
equation_adder(a, b, c, d, e, f);
getch();
}
void equation_adder(int p, int q, int r, int s, int t, int u)
{
int x, y, z;
x = p + s;
y = q + t;
z = r + u;
printf("\nThe addition of %dx^2+%dx+%d = 0 and %dx^2+%dx+%d = 0 is %dx^2=%dx+%d = 0",p,q,r,s,t,u,x,y,z);
}
