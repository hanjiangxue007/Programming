/*6.	Write a program to encode user input text and decode them.*/
#include<stdio.h>
#include<conio.h>
main()
{
char msg[100], encod[100], decod[100];
int i;
puts("Enter message to encode : ");
gets(msg);
for(i=0;msg[i]!='\0';i++)
{
encod[i] = msg[i] - 10; //any value can be placed.
}
encod[i] = '\0';
printf("\nEncoded message is :\n");
puts(encod);
for(i=0;encod[i] !='\0';i++)
{
decod[i] = encod[i] + 10;//same value should be placed.
}
printf("\nDecoded message is :\n");
puts(decod);
getch();
}
