/*10)	Write a program to input the marks of any 50 students in a subject and count how many students got above the average marks.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int marks[50],i,c,t;
	float avg;
	printf("\nEnter marks of any 50 students ");
	for(i=0;i<50;i++)
	{
		scanf("%d",&marks[i]);
	}
	printf("\n The marks are ");
	for(i=0;i<50;i++)
	{
		printf("%d ",marks[i]);
	}
	t=0;
	for(i=0;i<50;i++)
	{
		t=t+marks[i];
	}
	avg=t/50;
	c=0;
	for(i=0;i<50;i++)
	{
		if(marks[i]>avg)
		{
			c++;
		}
	}
	printf("\n The no. of students who got above average marks =%d",c);
	getch();
}