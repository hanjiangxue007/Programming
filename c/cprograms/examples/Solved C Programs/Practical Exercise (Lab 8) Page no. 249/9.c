/*9)	Write a program to display the following menu and ask the user to enter his/her choice and do the task accordingly.
a.	Append Record
b.	Read Record
c.	Update Record
d.	Delete Record
e.	Quit
*/
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
	int ch,x;
	char next='y';
	FILE *fp,*fp1;
	//to print menu
	printf("\n**********MENU**************");
	printf("\n1. Append Record");
	printf("\n2. Read Record");
	printf("\n3. Update Record");
	printf("\n4. Delete Record");
	printf("\n5. Quit");
	printf("\n\nEnter your choice ");
	scanf("%d",&ch);
	switch(ch)
	{
		case 1:
			fp=fopen("student.dat","a");
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
			break;
		case 2:
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
			break;
		case 3:
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
			break;
		case 4:
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
			break;
		case 5:
			exit(0);
		default:
			printf("\nYou entered invalid number for your choice ");
			printf("\nPlease, enter your choice between 1 to 5 ");
	}
	getch();
}
	
