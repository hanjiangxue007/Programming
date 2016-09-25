/*2.	Write a program to print the following pattern.
	1
	2	2
	3	3	3
	4	4	4	4
	5	5	5	5	5
	*/
#include<stdio.h>
#include<conio.h>
main()
{
	int a,b;
	printf("the required pattern is ");
	printf("\n");
	for(a=1;a<=5;a++)
	{
		for(b=1;b<=a;b++)
		{
			printf("%d\t",a);
		}
		printf("\n\n");
	}
	getch();
	return(0);
}