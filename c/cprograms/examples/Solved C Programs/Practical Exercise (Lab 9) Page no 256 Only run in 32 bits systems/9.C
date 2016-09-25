#include <graphics.h>
#include<stdio.h>
#include<conio.h>
void main( )
{
int gd, gm,i,j;
gd = DETECT;
initgraph(&gd, &gm, "C:\\TC\\bgi");
circle(200,200,50);
line(200,250,200,350);
line(200, 350, 180,450);
line(200,350,220,450);
line(200,265,150,270);
line(200,265,250,270);
getch();
closegraph();
restorecrtmode();
}
