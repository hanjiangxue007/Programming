/*11)	Write a program to input roll no, name and address of different students and display the records of those students whose first name begins from the letter ‘S’.*/
#include<stdio.h>
#include<conio.h>
main()
{
	struct student
	{
		int rn;
		char name[50];
		char adr[60];
	};
	struct student s[5];
	int i,n;
	//code to input
	printf("Enter the value of 'n' ");
	scanf("%d",&n);
	for(i=0;i<n;i++)
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
	printf("\n The name list of the students whose name begin from the letter 'S' ");
	printf("\n\nRoll No.\tName\tAddrress");
	for(i=0;i<5;i++)
	{
		if(s[i].name[0]=='S'||s[i].name[0]=='s')
		{
			printf("\n%d\t%s\t%s",s[i].rn,s[i].name,s[i].adr);
		}
	}
	getch();
	return(0);
}