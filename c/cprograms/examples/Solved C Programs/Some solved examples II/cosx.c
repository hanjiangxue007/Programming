/*Calculate the factorial of number recursively.From that calculate the value of
cos(x)=1-(x2/2!)+(x4/4!)-(....(xn/n!)*/
#include<stdio.h>
#include<conio.h>
#include<math.h>
int rec(int);
main()
{
 int x,n,i,j;
 float sum=0,z,s;
 printf("Enter the value of 'n':");
 scanf("%d",&n);
 printf("Enter the value of x:");
 scanf("%d",&x);
 for(i=1;2*(i-1)<=n;i++)
 {
 z=pow(x,2*(i-1)) * pow(-1,(i-1));
 sum=sum+(float)(z/rec(2*(i-1)));
 }
 printf("\n cos(x)=%f",sum);
getch();
}
int rec(j)
 {
 if(j==0)
 return 1;
 else
 return j* rec(j-1);
 }
