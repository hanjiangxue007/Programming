#include <graphics.h>
#include<stdio.h>
#include<conio.h>
void main( )
{
int gd, gm,i,j;
gd = DETECT;
initgraph(&gd, &gm, "C:\\TC\\bgi");
line(100,100, 200,100);
line(200,100,300,50);
line(300,50,400,50);
line(400,50,500,100);
line(500,100,550,100);
line(550,100,550,150);
line(550,150,450,150);
circle(425,150,25);
line(400,150,175,150);
circle(150,150,25);
line(125,150,100,150);
line(100,150,100,100);
getch();
closegraph();
restorecrtmode();
}
