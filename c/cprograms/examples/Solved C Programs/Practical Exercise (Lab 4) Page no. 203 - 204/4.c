/*4)	Write a program to input the age of ‘n’ numbers of students in a class and find the average age of the students in that class.*/
#include<stdio.h>
#include<conio.h>
#define N 1000
main()
{
	int age[N],i,t,n;
	float avg;
	printf("Enter the value of 'n' i.e. number of students ");
	scanf("%d",&n);
	printf("\nEnter the age of the students   ");
	for(i=0;i<n;i++)
	{
		scanf("%d",&age[i]);
	}
	printf("\n The age are ");
	for(i=0;i<n;i++)
	{
		printf("%d ",age[i]);
	}
	t=0;
	for(i=0;i<n;i++)
	{
		t=t+age[i];
	}
	avg=t/n;
	printf("\n The average age of students=%f",avg);
	getch();
}
