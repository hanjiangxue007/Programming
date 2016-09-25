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
if(ducks*2+ships*4 == 86)
{
printf("\nducks = %d and ships = %d", ducks, ships);
}
}
} 
getch();
}
