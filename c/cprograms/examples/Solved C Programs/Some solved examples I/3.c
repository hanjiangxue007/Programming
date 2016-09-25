/*3.	Write a C program to read a line of text and change it to lowercase.*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
main()
{
	char text[200];
	printf("Enter a line of text ");
	gets(text);
	strlwr(text);
	printf("The text in lower case : %s",text);
	getch();
}