/*4.	Write a C program to read a line of text and change it to lowercase without using string/library function.*/
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
		if(text[i]>='A' && text[i]<='Z')
		{
			text[i]=text[i]+32;
		}
	}
	printf("The text in lower case : %s",text);
	getch();
}