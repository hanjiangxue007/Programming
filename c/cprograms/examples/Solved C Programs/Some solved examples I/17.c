/*17.	Write a C program to  print all ASCII values of all the characters and display both.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int i;
	printf("\nASCII value\tCharacter");
	for(i=0;i<=255;i++)
	{
		printf("\n%d\t%c",i,i);
	}
	getch();
}