/*4)	Write a program to delete record from the data file created in Q.N.1.*/
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
	printf("\nEnter the roll no. of the student whose record you want to delete ");
	scanf("%d",&x);
	while(fread(&s,sizeof(s),1,fp)==1)
	{
		if(s.rn==x)
		{
			continue;
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
	
