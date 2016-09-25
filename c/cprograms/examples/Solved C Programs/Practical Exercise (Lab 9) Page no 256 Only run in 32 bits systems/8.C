#include <graphics.h>
#include<stdio.h>
#include<conio.h>
void main( )
{
int gd, gm,i,j;
gd = DETECT;
initgraph(&gd, &gm, "C:\\TC\\bgi");
line(100,100, 400,100);
line(400,100,400,400);
line(400,400,100,400);
line(100,400,100,100);
line(150,50,450,50);
line(450,50,450,350);
line(100,100,150,50);
line(400,100,450,50);
line(400,400,450,350);
getch();
closegraph();
restorecrtmode();
}
