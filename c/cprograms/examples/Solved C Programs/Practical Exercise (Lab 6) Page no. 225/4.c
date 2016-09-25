/*4)	Write a program to input names and addresses of any 50 persons and sort the records in ascending order on the basis of names.*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
main()
{
	//code to design structure
	struct person
	{
		char name[50];
		char adr[60];
	};
	//code to declare structure and other variable
	struct person p[50],t;
	int i,j;
	//code to input
	for(i=0;i<50;i++)
	{
		printf("\nEnter the name	:	");
		gets(p[i].name);
		printf("\nEnter the address   :		");
		gets(p[i].adr);
	}
	//code to display
	printf("\n\nName\tAddrress");
	for(i=0;i<50;i++)
	{
		printf("\n%s\t%s",p[i].name,p[i].adr);
	}
		//code to sort
	for(i=0;i<50;i++)
	{
		for(j=0;j<49;j++)
		{
			if(strcmpi(p[j].name,p[j+1].name)>0)
			{
				t=p[j];
				p[j]=p[j+1];
				p[j+1]=t;
			}
		}
	}
	//code to display after sorting
	printf("\n\nName\tAddrress");
	for(i=0;i<50;i++)
	{
		printf("\n%s\t%s",p[i].name,p[i].adr);
	}
	getch();
	return(0);
}