/*15.	Write a program to input any two words and find they are same words or not.*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
main()
{
	char text1[100],text2[100];
	printf("Enter first word ");
	gets(text1);
	printf("Enter second word ");
	gets(text2);
	if(strcmpi(text1,text2)==0)
	{
		printf("Yes, the words are similar ");
	}
	else
	{
		printf("No, the words are not similar ");
	}
	getch();
}
