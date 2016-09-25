/*12.	Write a program to input a word and reverse it by using library function.*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
main()
{
	char text[200];
	printf("Enter a line of text ");
	gets(text);
	strrev(text);
	printf("The text in reverse order : %s",text);
	getch();
}