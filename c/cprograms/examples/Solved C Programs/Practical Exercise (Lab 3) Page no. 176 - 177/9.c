/*9.	Write a C program to display the sum of 'n' terms of even numbers.*/
#include<stdio.h>
#include<conio.h>
main()
{
int i, n, evnsum=0;
printf("\nEnter how many terms : ");
scanf("%d", &n);
for(i=0;i<=n;i+=2)
{
evnsum += i;
}
printf("\nThe sum of even numbers upto %d is %d", n, evnsum );
getch();
}
