/*6) Rita has a money pouch containing Rs.700. 
There are equal number of 25 paise coins, 50 paise and one rupee coins. 
Write a C program to find how many of each are there?
*/
#include<stdio.h>
#include<conio.h>
main()
{
int r=700,tot;
float c=.50+.25+1;
tot=r/c;
printf("1 RS coins are %d, 50 Paisa coins are %d and 25 Paisa coins are %d and total amount is %.0f",tot, tot, tot,tot*c);
getch();
}
