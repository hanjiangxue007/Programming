/*5.	Write a program to read a line of text and count the length of the text including blank space and punctuation marks using library function.*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
main()
{
	char text[200];
	int len;
	printf("Enter a line of text ");
	gets(text);
	len=strlen(text);
	printf("The length of the text= %d",len);
	getch();
}