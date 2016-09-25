/*There are some goats and ducks in a farm. There are 60 eyes and 86 foot 
in total. Write a program to find number of goats and ducks in the farm.*/
#include<stdio.h>
#include<conio.h>
main()
{
 int eyes = 60, legs = 86, ducks, ships, animals;
animals = eyes /2; //every has two eyes i.e. 30 total
for(ducks = 0; ducks<=30; ducks++)
{
for(ships =0; ships <=30;ships++)
{
if((ducks*2+ships*4 == 86)&&(ducks+ships)*2 == 60)
{
printf("\nThe number of ducks = %d and ships = %d having (%d + %d) * 2 = %d eyes and %d * 2 + %d * 4 = %d foots", ducks, ships, ducks, ships, (ducks+ships)*2,ducks, ships, ducks*2+ships*4);
}
}
} 
getch();
}
