/*13.	Write a C program to check user input word is palindrome or not? [Palindrome words are same by reading from bother directions. For example: madam, civic, level, mom, noon, racecar, refer, rotator, rotor etc.]*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
main()
{
	char text1[100],text2[100];
	printf("Enter a word ");
	gets(text1);
	strcpy(text2,text1);
	strrev(text1);
	if(strcmpi(text1,text2)==0)
	{
		printf("Yes, the word is palindrome ");
	}
	else
	{
		printf("No, the word is not palindrome ");
	}
	getch();
}
