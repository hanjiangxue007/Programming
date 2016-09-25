#include <graphics.h>
#include<stdio.h>
#include<conio.h>
void main( )
{
int gd, gm, x, y,i;
gd = DETECT;
initgraph(&gd, &gm, "C:\\TC\\bgi");
x= getmaxx();
y = getmaxy();

for(i=1;i<=y;i+=5)
{
rectangle(x/2-i,y/2-i,x/2+i,y/2+i);
}
getch();
closegraph();
restorecrtmode();
}
