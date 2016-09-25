#include<stdio.h>
 void main()
 {
 int num,x,y,a[50][50];
 clrscr();
 fflush(stdin);
 
printf("Enter the number of rows: ");
 scanf("%d",&num);
 
printf("\n\t\tPascal's Triangle of Order %d\n\n",num);
 
for(x=0;x<num;x++)
 {
 for(y=0;y<=x;y++)
 {
 if(x==y || y==0)
 a[x][y]=1;
 else
 a[x][y]=a[x-1][y-1]+a[x-1][y];
 printf("%4d",a[x][y]);
 }
 printf("\n\n");
 }
 
getch();
 }
 
