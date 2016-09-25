/*13.	A number of "Cats" got together and decided to kill between them 999919 mice. 
Every cat killed equal number of "mice". Write a program to find number of cats.*/
#include<stdio.h>
#include<conio.h>
main()
{
int mice=999919,cats;
printf("\nPossible combinations of\n\nCats\t\tMice\n\n ");
for(cats=2;cats<=999919;cats++)
{
 if(mice%cats==0)
 {
 printf("%d\t\t%d\n",cats, mice);
}
}
getch();
}


