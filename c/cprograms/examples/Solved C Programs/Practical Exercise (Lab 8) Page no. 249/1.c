/*1)	Write a program to input roll no, name and address of different students and write them in a data file.*/
#include<stdio.h>
#include<conio.h>
main()
{
	struct student
	{
		int rn;
		char name[40];
		char adr[60];
	}s;
	char next='y';
	FILE *fp;
	fp=fopen("student.dat","w");
	if(fp==NULL)
	{
		printf("\nFile creation error ");
		getch();
		exit(0);
	}
	
	while(next=='y'||next=='Y')
	{
		printf("\nEnter the roll no. ");
		scanf("%d",s.rn);
		fflush(stdin);
		printf("\nEnter the name  ");
		gets(s.name);
		printf("\nEnter the address ");
		gets(s.adr);
		fwrite(&s,sizeof(s),1,fp);
		printf("\n\n Do you want to write the record of next student (Y/N)?  ");
		next=getche();
	}
	fclose(fp);
	getch();
}
	