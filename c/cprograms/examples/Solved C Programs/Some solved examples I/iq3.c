/*10) Write a C program to find a two digit number, 
the second digit of which is smaller than its first digit by 4, 
and if the number was divided by the digit's sum, the quotient would be 7.
*/
#include<stdio.h>
#include<conio.h>
main()
{
int i, s,f;
for(i=10;i<=99;i++)
{
s=i%10;
f=i/10;
if(((s-4)==f)&&(i%(f+s))==7)
printf("\nthe first numbe of %d is %d which smaller than %d by 4 and remainder after dividing by %d is 7",i, f, s, f+s);
}
getch();
}
