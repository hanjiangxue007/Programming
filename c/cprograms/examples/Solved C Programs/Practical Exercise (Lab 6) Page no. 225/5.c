/*5)	Write a C program to read 20 patients id, name, disease and sort them on the basis of disease.*/
#include<stdio.h>
#include<conio.h>
#include<string.h>
main()
{
	struct patient
	{
		int pid;
		char name[40];
		char disease[100];
	}p[20],t;
	int i,j;
	//input
	for(i=0;i<20;i++)
	{
		printf("\nEnter the patient id ");
		scanf("%d",&p[i].pid);
		fflush(stdin);
		printf("\nEnter the patient name ");
		gets(p[i].name);
		printf("\nEnter the patient's disease ");
		gets(p[i].disease);
	}
	//sort
	for(i=0;i<20;i++)
	{
		for(j=0;j<19;j++)
		{
			if(strcmpi(p[j].disease,p[j+1].disease)>0)
			{
				t=p[j];
				p[j]=p[j+1];
				p[j+1]=t;
			}
		}
	}
	//display
	printf("\nPatientId\tPatient Name\tDisease");
	for(i=0;i<20;i++)
	{
		printf("\t%d\t%s\t%s",p[i].pid,p[i].name,p[i].disease);
	}
	getch();
}