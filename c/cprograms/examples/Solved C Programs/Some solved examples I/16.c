/*16.	Write a program to input any two words and find they are same words or not without using string function.*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
main()
{
	char text1[100],text2[100];
	int i;
	char same;
	printf("Enter first word ");
	gets(text1);
	printf("Enter second word ");
	gets(text2);
	
	if(strlen(text1)==strlen(text2))
	{
		for(i=0;i<strlen(text1);i++)
		{
			if(text1[i]==text2[i])
			{
				continue;
			}
			else
			{
				same='n';
				break;
			}
		}
		if(same=='n')
		{
			printf("\nNo, the two words are not similar ");
		}
		else
		{
			printf("\Yes, the words are similar ");
		}
		
	}
	else
	{
		printf("No, the words are not similar ");
	}
	getch();
}