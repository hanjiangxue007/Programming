/*2.	Write a program to read a line of text and convert into upper case without using string/library function.*/
#include<stdio.h>
#include<conio.h>
main()
{
	char text[200];
	int i;
	printf("Enter a line of text ");
	gets(text);
	for(i=0;text[i]!='\0';i++)
	{
		if(text[i]>='a' && text[i]<='z')
		{
			text[i]=text[i]-32;
		}
	}
	printf("The text in Upper case : %s",text);
	getch();
}