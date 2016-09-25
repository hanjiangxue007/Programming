/*14.	There are some goats and ducks in a farm. There are 60 eyes and 86 foot in total. 
Write a program to find number of goats and ducks in the farm.*/
#include<stdio.h>
#include<conio.h>
main()
{
 int eyes = 60, legs = 86, ducks, ships, animals;
animals = eyes /2; //every has two eyes i.e. 30 total
printf("\nThe possible combinations is: ");
for(ducks = 0; ducks<=30; ducks++)
{
for(ships =0; ships <=30;ships++)
{
if(ducks*2+ships*4 == 86 && (ducks+ships)*2 == 60)
{
printf("\nducks = %d and ships = %d having %d eyes and %d foot", ducks, ships, (ducks+ships)*2, ducks*2+ships*4);
}
}
} 
getch();
}


