/*10)	Write a program to input name, district and phone no. of  the students in a college and display the students of those students who are from ‘Chitwan’ district.*/
#include<stdio.h>
#include<conio.h>
#define N 500
main()
{
	struct student
	{
		char name[50];
		char district[60];
		char ph[13];
	};
	struct student s[N];
	int i,n;
	//code to input
	printf("\nEnter the value of 'n'  ");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		printf("\nEnter the name	:	");
		gets(s[i].name);
		printf("\nEnter the address	:	");
		gets(s[i].district);
		printf("\nEnter the phone no.   :		");
		gets(s[i].ph);
	}
	//code to display 
	printf("\n\nThe name list of the students who are from Chitwan district are ");
	printf("\n\nName\tDistrict\tPhone No.");
	for(i=0;i<n;i++)
	{
		if(strcmpi(s[i].district,"Chitwan")==0)
		{
			printf("\n%s\t%s\t%s",s[i].name,s[i].district,s[i].ph);
		}
	}
	getch();
	return(0);
}
