#include<stdio.h>
#include<conio.h>
main()
{
int a=5, b=11;
printf("Bitwise %d AND %d is %d\n",a,b,a&b);
printf("Bitwise %d OR %d is %d\n",a,b,a|b);
printf("Bitwise NOT of %d is %d\n",a, ~a);
printf("Bitwise %d XOR %d is %d\n",a,b,a^b);
printf("Bitwise left shift of %d with 2 is %d\n",a, a<<2);
printf("Bitwise right shift of %d with 2 is %d\n",a, a>>2);
getch();
}
