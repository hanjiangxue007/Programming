/*3)	Write a program to input roll number, name and age of different students and sort the record in ascending order on the basis of age.*/
#include<stdio.h>
#include<conio.h>
#define N 500
main()
{
	//code to design structure
	struct student
	{
		int rn;
		char name[50];
		int age;
	};
	//code to declare structure and other variable
	struct student s[N],t;
	int i,j,n;
	//code to input value of n
	printf("\nEnter the value of 'n'  :   ");
	scanf("%d",&n);
	//code to input
	for(i=0;i<n;i++)
	{
		printf("\nEnter the roll no.  :  ");
		scanf("%d",&s[i].rn);
		fflush(stdin);
		printf("\nEnter the name	:	");
		gets(s[i].name);
		printf("\nEnter the age   :		");
		gets(s[i].age);
	}
	//code to display before sorting
	printf("\n\nRoll No.\tName\tAge");
	for(i=0;i<n;i++)
	{
		printf("\n%d\t%s\t%s",s[i].rn,s[i].name,s[i].age);
	}
	//code to sort
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-1;j++)
		{
			if(s[j].age>s[j+1].age)
			{
				t=s[j];
				s[j]=s[j+1];
				s[j+1]=t;
			}
		}
	}
	//code to display after sorting
	printf("\n\nRoll No.\tName\tAge");
	for(i=0;i<n;i++)
	{
		printf("\n%d\t%s\t%s",s[i].rn,s[i].name,s[i].age);
	}
	
	getch();
	return(0);
}