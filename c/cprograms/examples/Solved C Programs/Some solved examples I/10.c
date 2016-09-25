/*10.	Write a program to read a line of text and count how many English vowels and consonants alphabets are there.*/
 #include<stdio.h>
#include<conio.h>
main()
{
	char text[200];
	int i,totalphabets, totvowel,totconsonant;
	printf("Enter a line of text ");
	gets(text);
	totalphabets=0;
	for(i=0;text[i]!='\0';i++)
	{
		if((text[i]>='A'&& text[i]<='Z')||(text[i]>='a'&& text[i]<='z'))
		{
			totalphabets++;
		}		
	}
 totvowel=0;
	for(i=0;text[i]!='\0';i++)
	{
		if(text[i]=='A'|| text[i]=='a'||text[i]=='E'|| text[i]=='e'||text[i]=='I'|| text[i]=='i'||text[i]=='O'|| text[i]=='o'||text[i]=='U'|| text[i]=='u')
		{
			totvowel++;
		}		
	}
	totconsonant=totalphabets-totvowel;
	printf("\n The total no. of vowels alphabets in the given text=%d",totvowel);
	printf("\n the total no. of consonants alphabets in the given text=%d",totconsonant);
	getch();
}
