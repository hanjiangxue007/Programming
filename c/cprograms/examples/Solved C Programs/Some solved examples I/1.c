/*1.	Write a program to read a line of text and to convert it into uppercase. */
#include<stdio.h>
#include<conio.h>
#include<string.h>
main()
{
	char text[200];
	printf("Enter a line of text ");
	gets(text);
	strupr(text);
	printf("The text in Upper case : %s",text);
	getch();
}