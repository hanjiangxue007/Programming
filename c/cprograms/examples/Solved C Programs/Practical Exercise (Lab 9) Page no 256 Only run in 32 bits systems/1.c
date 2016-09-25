/*1.	Write a graphical C program to print circle in loop and show as an animation. */
#include <graphics.h>
#include<stdio.h>
#include<conio.h>
void main()
{
int gd, gm, x, y,i;
gd = DETECT;
initgraph(&gd, &gm, "C:\\TC\\bgi");
x= getmaxx();
y = getmaxy();
for(i=1;i<=y;i+=10)
{
circle(x/2,y/2,i+10,i);
}
getch();
closegraph();	
restorecrtmode();
