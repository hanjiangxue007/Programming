/*11.	Write a program to input names of 'n' number of students into 2 dimensional array and sort them in alphabetical order. */
#include<stdio.h>
#include<conio.h>
#include<string.h>
#define N 500
main()
{
	char name[N][50], t[50];
	int i,j,n;
	printf("Enter the value of 'n'  ");
	scanf("%d",&n);
	fflush(stdin);
	printf("\nEnter the name of the %d students",n);
	for(i=0;i<n;i++)
	{
		gets(name[i]);
	}
	//code to sort
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-1;j++)
		{
			if(strcmpi(name[j],name[j+1])>0)
			{
				strcpy(t,name[j]);
				strcpy(name[j],name[j+1]);
				strcpy(name[j+1],t);
			}
		}
	}
	//code to display after sorting
	printf("\n the name of student in ascending order ");
	for(i=0;i<n;i++)
	{
		printf("\n%s",name[i]);
	}
	getch();
}
