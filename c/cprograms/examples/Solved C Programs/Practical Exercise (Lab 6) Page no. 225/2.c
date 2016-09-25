/*2)	Write a C program to store roll number, name, address and phone number of 10 students by using union and display the record, see what happen on display.*/
#include<stdio.h>
#include<conio.h>
main()
{
	//code to design structure
	union student
	{
		int rn;
		char name[50];
		char adr[60];
		char phone[10];
	};
	//code to declare structure and other variable
	union student s[10];
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