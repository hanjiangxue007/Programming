/*7)	Write a program to input the names and age of any 100 students and count how many students are in the age group between 15 to 20.*/
#include<stdio.h>
#include<conio.h>
main()
{
	struct student
	{
		char name[50];
		int age;
	};
	struct student s[100];
	int i,c;
	//code to input
	for(i=0;i<100;i++)
	{
		fflush(stdin);
		printf("\nEnter the name	:	");
		gets(s[i].name);
		printf("\nEnter the age   :		");
		scanf("%d",s[i].age);
	}
	//code to display 
	printf("\n\nRoll No.\tName\tAge");
	for(i=0;i<100;i++)
	{
		printf("\n%s\t%s",s[i].name,s[i].age);
	}
	//code to count
	c=0;
	for(i=0;i<100;i++)
	{
		if(s[i].age>=15 && s[i].age<=20)
		{
			c++;
		}
	}
	printf("\n The total no. of students in the age group of 15 to 20 years=%d",c);
	getch();
	return(0);
}
