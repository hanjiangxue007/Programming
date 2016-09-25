/*6.	 Write a program to read a line of text and count the length of the text including blank space and punctuation marks without using library function.*/
#include<stdio.h>
#include<conio.h>
main()
{
	char text[200];
	int i,len;
	printf("Enter a line of text ");
	gets(text);
	len=0;
	for(i=0;text[i]!='\0';i++)
	{
		len++;
		
	}
	printf("The length of the text= %d",len);
	getch();
}
