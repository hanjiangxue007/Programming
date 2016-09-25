/*9)	Write a program to input the name, address and age of different persons in a village and display the records who are eligible to cast vote. [note: the persons who are 18years or above are eligible to cast vote.]*/
#include<stdio.h>
#include<conio.h>
#define N 500
main()
{
	struct record
	{
		char name[50];
		char adr[60];
		int age;
	};
	struct record r[N];
	int i,n;
	//code to input
	printf("\nEnter the value of 'n'  ");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		fflush(stdin);
		printf("\nEnter the name	:	");
		gets(r[i].name);
		printf("\nEnter the address	:	");
		gets(r[i].adr);
		printf("\nEnter the age   :		");
		gets(r[i].age);
	}
	//code to display before sorting
	printf("\n\nThe name list of the persons who are eligible to cast vote are ");
	printf("\n\nName\tAddress\tAge");
	for(i=0;i<n;i++)
	{
		if(r[i].age>=18)
		{
			printf("\n%s\t%s\t%d",r[i].name,r[i].adr,r[i].age);
		}
	}
	getch();
	return(0);
}
