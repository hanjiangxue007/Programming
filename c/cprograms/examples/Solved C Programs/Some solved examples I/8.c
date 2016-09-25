/*8.	Write a program to read a line of text and count how many times the letter ‘A’ or ‘a’ has occurred.*/
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
		if(text[i]=='A'|| text[i]=='a')
		{
			len++;
		}		
	}
	printf("The no. of 'a' or 'A' in the given text = %d",len);
	getch();
}
