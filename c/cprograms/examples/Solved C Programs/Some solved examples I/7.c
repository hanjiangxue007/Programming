/*7.	Write a program to read a line of text and count only the English alphabets.
 [Note: your program should not count the blank space and any punctuation marsk.]*/
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
		if((text[i]>='A'&& text[i]<='Z')||(text[i]>='a'&& text[i]<='z'))
		{
			len++;
		}		
	}
	printf("The no. of english alphabets = %d",len);
	getch();
}
