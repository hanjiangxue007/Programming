/*8)	Write a program to delete the record of the employee stored in Q.N.5.*/
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
	int x;
	FILE *fp,*fp1;
	fp=fopen("emp.dat","r");
	fp1=fopen("newfp1.dat","w");
	if(fp==NULL)
	{
		printf("\nFile creation error ");
		getch();
		exit(0);
	}
	printf("\nEnter the employee code whose record you want to delete ");
	scanf("%d",&x);
	while(fread(&e,sizeof(e),1,fp)==1)
	{
		if(x==e.ecode)
		{
			continue;
		}
		else
		{
			fwrite(&e,sizeof(e),1,fp1);
		}
	}
	fclose(fp);
	fclose(fp1);
	remove("emp.dat");
	rename("newemp.dat","emp.dat");
	getch();
}