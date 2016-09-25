/*8)	Write a program to input the names and districts of the different employees and 
arrange the records of the employees on the basis of their districts.*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
#define N 500
main()
{
	struct employee
	{
		char name[50];
		char district[60];
	};
	struct employee e[N],t;
	int i,j,n;
	//code to input
	printf("\nEnter the value of 'n' ");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		printf("\nEnter the name	:	");
		gets(e[i].name);
		printf("\nEnter the name of district   :		");
		gets(e[i].district);
	}
	//code to display
	printf("\n\nName\tDistrict");
	for(i=0;i<n;i++)
	{
		printf("\n%s\t%s",e[i].name,e[i].district);
	}
		//code to sort
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-1;j++)
		{
			if(strcmpi(e[j].district,e[j+1].district)>0)
			{
				t=e[j];
				e[j]=e[j+1];
				e[j+1]=t;
			}
		}
	}
	//code to display after sorting
	printf("\n\nName\tDistrict");
	for(i=0;i<50;i++)
	{
		printf("\n%s\t%s",e[i].name,e[i].district);
	}
	getch();
	return(0);
}