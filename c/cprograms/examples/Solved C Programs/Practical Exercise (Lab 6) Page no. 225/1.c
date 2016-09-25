/*1)	Write a program to input Roll No., name and address of any 5 students in structure and display the records properly.*/
#include<stdio.h>
#include<conio.h>
main()
{
	//code to design structure
	struct student
	{
		int rn;
		char name[50];
		char adr[60];
	};
	//code to declare structure and other variable
	struct student s[5];
	int i;
	//code to input
	for(i=0;i<5;i++)
	{
		printf("\nEnter the roll no.  :  ");
		scanf("%d",&s[i].rn);
		fflush(stdin);
		printf("\nEnter the name	:	");
		gets(s[i].name);
		printf("\nEnter the address   :		");
		gets(s[i].adr);
	}
	//code to display
	printf("\n\nRoll No.\tName\tAddrress");
	for(i=0;i<5;i++)
	{
		printf("\n%d\t%s\t%s",s[i].rn,s[i].name,s[i].adr);
	}
	getch();
	return(0);
}