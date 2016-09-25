/*18)	Write a program to input the marks of any 100 students in a subject and find the highest and lowest marks.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int marks[100],i,h,l;
	printf("\nEnter  marks of 100 students ");
	for(i=0;i<100;i++)
	{
		scanf("%d",&marks[i]);
	}
	printf("\n The marks are ");
	for(i=0;i<100;i++)
	{
		printf("%d ",marks[i]);
	}
	//code to find highest marks
	h=marks[0];
	for(i=0;i<50;i++)
	{
		if(marks[i]>h)
		{
			h=marks[i];
		}
	}
	//code to find lowest marks
	l=marks[0];
	for(i=0;i<50;i++)
	{
		if(marks[i]<l)
		{
			l=marks[i];
		}
	}
	printf("\n the biggest marks=%d",h);
	printf("\n the lowest marks=%d",l);
	getch();
}