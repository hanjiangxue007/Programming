/*2.	The marks obtained by a student in 7 different subjects are entered through the keyboard. The student gets a division as per the following rules: 	[10]
Percentage greater or equal to 60	First Division
Percentage between 45 and 59	Second Division
Percentage between 35 and 44	Third Division
Percentage less than 35 	Fail
Marks less than 35 in a subject will be declared as   	Fail
*/

#include<stdio.h>
#include<conio.h>
#include<string.h>
main()
{
	int s1,s2,s3,s4,s5,s6,s7,total;
	float percent;
	char res[10],div[30];
	printf("\nEnter the marks of first subject ");
	scanf("%d",&s1);
	printf("\nEnter the marks of second subject ");
	scanf("%d",&s2);
	printf("\nEnter the marks of third subject ");
	scanf("%d",&s3);
	printf("\nEnter the marks of fourth subject ");
	scanf("%d",&s4);
	printf("\nEnter the marks of fifth subject ");
	scanf("%d",&s5);
	printf("\nEnter the marks of sixth subject ");
	scanf("%d",&s6);
	printf("\nEnter the marks of seventh subject ");
	scanf("%d",&s7);
	//code to find total
	total=s1+s2+s3+s4+s5+s6+s7;
	//code to find percent and result
	if(s1>=35&&s2>=35&&s3>=35&&s4>=35&&s5>=35 &&s6>=35&&s7>=35)
	{
		percent=(float)total*100/700;
		strcpy(res,"Pass");
	}
	else
	{
		percent=0;
		strcpy(res,"Fail");
	}
	//code to find division
	if(percent>=60)
	{
		strcpy(div,"First Division");
	}
	else if(percent>=45)
	{
		strcpy(div,"Second Division");
	}
	else if(percent>=35)
	{
		strcpy(div,"Third Division");
	}
	else
	{
		strcpy(div,"Fail");
	}
	//code to display total, percent, result and division
	printf("\nTotal marks=%ld",total);
	printf("\n Percentage =%.2f",percent);
	printf("\n Result= %s",res);
	printf("\n Division=%s",div);
	getch();
}
	
