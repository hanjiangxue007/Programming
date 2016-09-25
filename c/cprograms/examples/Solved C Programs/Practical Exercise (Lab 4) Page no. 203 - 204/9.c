/*9)Write a program to input the marks of any 100 students in computer science and count how many students got marks in the range of 70 to 90.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int marks[100],i,c;
	printf("\nEnter the marks 100 students ");
	for(i=0;i<100;i++)
	{
		scanf("%d",&marks[i]);
	}
	printf("\n The marks are ");
	for(i=0;i<100;i++)
	{
		printf("%d ",marks[i]);
	}
	c=0;
	for(i=0;i<100;i++)
	{
		if(marks[i]>=70 && marks[i]<=90)
		{
			c++;
		}
	}
	printf("\n The no. of students who got marks in the range of 70 to 90 are=%d",c);
	getch();
}