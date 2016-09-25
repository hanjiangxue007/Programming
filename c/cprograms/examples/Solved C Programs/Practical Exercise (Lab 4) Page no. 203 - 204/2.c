/*2)	Write a program to input the marks of any 20 students in Computer Science and find the average marks.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int marks[20],i,t;
	float avg;
	printf("\nEnter the marks of any 20 students in computer science  ");
	for(i=0;i<20;i++)
	{
		scanf("%d",&marks[i]);
	}
	printf("\n The marks are ");
	for(i=0;i<20;i++)
	{
		printf("%d ",marks[i]);
	}
	t=0;
	for(i=0;i<20;i++)
	{
		t=t+marks[i];
	}
	avg=t/20;
	printf("\n The average marks in computer science=%f",avg);
	getch();
}