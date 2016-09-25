/*11)	Write a program to input marks of any 40 students in a subjects and count how many students are passed in Distinction, First Division, Second Division, Third Division and Failed. 
Marks		Division
>=75		Distinction
>=60		First 
>=45		Second
>=35		Third
Below 35	Fail
*/
#include<stdio.h>
#include<conio.h>
main()
{
	int marks[40],i,c1,c2,c3,c4,c5;
	printf("\nEnter marks of any 40 students ");
	for(i=0;i<40;i++)
	{
		scanf("%d",&marks[i]);
	}
	printf("\n The marks are ");
	for(i=0;i<40;i++)
	{
		printf("%d ",marks[i]);
	}
	c1=c2=c3=c4=c5=0;
	for(i=0;i<40;i++)
	{
		if(marks[i]>=75)
		{
			c1++;
		}
		else if(marks[i]>=60)
		{
			c2++;
		}
		else if(marks[i]>=45)
		{
			c3++;
		}
		else if(marks[i]>=35)
		{
			c4++;
		}
		else
		{
			c5++;
		}
		
	}
	printf("\n The no. of students passed in Distinction=%d",c1);
	printf("\n The no. of students passed in First Division=%d",c2);
	printf("\n The no. of students passed in Second Division=%d",c3);
	printf("\n The no. of students passed in third Division=%d",c4);
	printf("\n The no. of students who got failed=%d",c5);
	getch();
}
