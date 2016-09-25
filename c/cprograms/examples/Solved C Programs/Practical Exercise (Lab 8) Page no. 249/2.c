/*2)	Write a program to read the data from the data file created in Q.N. 1 and display the records appropriately on the screen.*/
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
	FILE *fp;
	fp=fopen("student.dat","r");
	if(fp==NULL)
	{
		printf("\nFile opening error ");
		getch();
		exit(0);
	}
	printf("\nRoll No\tName\tAddress");
	while(fread(&s,sizeof(s),1,fp)==1)
	{
		printf("\n%d\t%s\t%s",s.rn,s.name,s.adr);
	}
	fclose(fp);
	getch();
}
	
