#include <graphics.h>
#include<stdio.h>
#include<conio.h>
void main( )
{
int gd, gm, x, y;
gd = DETECT;
initgraph(&gd, &gm, "C:\\TC\\bgi");
x= getmaxx();
y = getmaxy();
x = x/2;
y = y/2;
circle(x,y,y);
getch();
closegraph();
restorecrtmode();
}
