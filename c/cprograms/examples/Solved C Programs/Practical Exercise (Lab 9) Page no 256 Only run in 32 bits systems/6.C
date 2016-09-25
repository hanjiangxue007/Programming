#include <graphics.h>
#include<stdio.h>
#include<conio.h>
void main( )
{
int gd, gm, x, y,i,j;
gd = DETECT;
initgraph(&gd, &gm, "C:\\TC\\bgi");
x= getmaxx();
y = getmaxy();
x = x/2;
y = y/2;
for(i=y;i>0;i=i-3)
{
circle(x,y,i);
}
getch();
closegraph();
restorecrtmode();
}
