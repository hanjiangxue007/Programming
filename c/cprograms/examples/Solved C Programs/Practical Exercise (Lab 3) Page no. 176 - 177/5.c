/*5.	Write a C program to show the number in power of 2 up to N.*/
#include<stdio.h>
#include<math.h>
#include<conio.h>
main()
{
long int i, n;
long int ans;
printf("\nEnter how many terms : ");
scanf("%d",&n);
for(i=0;i<=n;i++)
{
ans = pow(2,i);
printf("\nThe %d times power of 2 is %ld",i,ans);
}
getch();
}
