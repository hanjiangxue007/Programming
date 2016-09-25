/*6)	Write a program to display records of the employees stored in Q.N.5.*/
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
	FILE *fp;
	fp=fopen("emp.dat","r");
	if(fp==NULL)
	{
		printf("\nFile opening error ");
		getch();
		exit(0);
	}
	printf("\nEmployeeCode\tName\tPost\tMonthly Salary");
	while(fread(&e,sizeof(e),1,fp)==1)
	{
		printf("\n%d\t\t%s\t%s\t%d",e.ecode,e.name,e.post,e.msal);
	}
	fclose(fp);
	getch();
}
	