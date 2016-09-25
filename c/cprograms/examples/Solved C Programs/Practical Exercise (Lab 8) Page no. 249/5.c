/*5)	Write a program to enter employee code, name, post and monthly salary of different employees and write then in a data file.*/
#include<stdio.h>
#include<conio.h>
main()
{
	struct employee
	{
		int ecode;
		char name[40];
		char post[30];
		int msal;
	}e;
	char next='y';
	FILE *fp;
	fp=fopen("emp.dat","w");
	if(fp==NULL)
	{
		printf("\nFile creation error ");
		getch();
		exit(0);
	}
	
	while(next=='y'||next=='Y')
	{
		printf("\nEnter the employee code ");
		scanf("%d",e.ecode);
		fflush(stdin);
		printf("\nEnter the name  ");
		gets(e.name);
		printf("\nEnter the post ");
		gets(e.post);
		printf("\nEnter the monthly salary ");
		scanf("%d",e.msal);
		fwrite(&e,sizeof(e),1,fp);
		printf("\n\n Do you want to write the record of next student (Y/N)?  ");
		next=getche();
	}
	fclose(fp);
	getch();
}
	
