/*9.	Write a program to read a line of text and count how many English vowels alphabets are there.*/
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
		if(text[i]=='A'|| text[i]=='a'||text[i]=='E'|| text[i]=='e'||text[i]=='I'|| text[i]=='i'||text[i]=='O'|| text[i]=='o'||text[i]=='U'|| text[i]=='u')
		{
			len++;
		}		
	}
	printf("The no. of vowels alphabets = %d",len);
	getch();
}
