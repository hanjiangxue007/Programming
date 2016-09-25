/* 6.	To input a positive integer and find it is a perfect cube number or not.*/
#include<stdio.h>
#include<conio.h>
main()
{
int n, i;
printf("\nEnter any number to check perfect cube or not : ");
scanf("%d",&n);
for(i=1;i<n;i++)
{
if(i*i*i == n) 
{
printf("\n %d is perfect cube number",n);
break;
}
}
if(i==n)
printf("\n%d number is not perfect cuber number",n);
getch();
}
