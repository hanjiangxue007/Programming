/*3)	Write a program to update the record in the data file created in Q.N.1.*/
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
	int x;
	FILE *fp,*fp1;
	fp=fopen("std.dat","r");
	fp1=fopen("newstd.dat","w");
	
	if(fp==NULL||fp1==NULL)
	{
		printf("\nFile creation error ");
		getch();
		exit(0);
	}
	printf("\nEnter the roll no. of the student whose record you want to update ");
	scanf("%d",&x);
	while(fread(&s,sizeof(s),1,fp)==1)
	{
		if(s.rn==x)
		{
			printf("\nEnter the roll no. ");
			scanf("%d",s.rn);
			fflush(stdin);
			printf("\nEnter the name  ");
			gets(s.name);
			printf("\nEnter the address ");
			gets(s.adr);
			fwrite(&s,sizeof(s),1,fp1);
		}
		else
		{
			fwrite(&s,sizeof(s),1,fp1);
		}
	}
	fclose(fp);
	fclose(fp1);
	remove("std.dat");
	rename("newstd.dat","std.dat");
	getch();
}
