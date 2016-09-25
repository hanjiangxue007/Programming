/*19)	Write a program to input the age of any 100 students and find the oldest age.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int age[100],i,oldage;
	printf("\nEnter the age of 100 students ");
	for(i=0;i<100;i++)
	{
		scanf("%d",&age[i]);
	}
	printf("\n The age of 100 students  ");
	for(i=0;i<100;i++)
	{
		printf("%d ",age[i]);
	}
	oldage=age[0];
	for(i=0;i<100;i++)
	{
		if(age[i]>oldage)
		{
			oldage=age[i];
		}
	}
	printf("\n The oldest age=%d",oldage);
	getch();
}