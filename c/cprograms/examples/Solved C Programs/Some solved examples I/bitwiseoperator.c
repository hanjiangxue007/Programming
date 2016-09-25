/*Write a C program to demonstrate the use of bitwise AND , OR, NOT, XOR and shift operators. */
#include<stdio.h>
#include<conio.h>
main()
{
int i=5,j=11;
printf("\nBitwise AND between %d and %d is %d",i,j,i&j);
printf("\nBitwise OR between %d and %d is %d", i,j, i|j);
printf("\nBitwise NOT of %d is %d and Bitwise not of %d is %d", i, ~i,j,~j);
printf("\nBitwise right shift of %d twise is %d",i,i>>2);
printf("\nBitwise left shift of %d thrice is %d",j,j<<3);
getch();
}
