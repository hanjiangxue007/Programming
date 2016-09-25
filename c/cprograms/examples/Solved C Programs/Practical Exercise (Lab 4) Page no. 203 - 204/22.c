/*22)	Write a program to input the height of ‘n’ numbers in an array and display the height in shortest to tallest form.*/
#include<stdio.h>
#include<conio.h>
#define N 1000
main()
{
	int height[N],i,j,t,n;
	printf("Enter the value of 'n' ");
	scanf("%d",&n);
	printf("\nEnter the height of n students ");
	for(i=0;i<n;i++)
	{
		scanf("%d",&height[i]);
	}
	printf("\n The height of the students before sorting are ");
	for(i=0;i<n;i++)
	{
		printf("%d ",height[i]);
	}
	//code to sort
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-1;j++)
		{
			if(height[j]<height[j+1])
			{
				t=height[j];
				height[j]=height[j+1];
				height[j+1]=t;
			}
		}
	}
	printf("\n The height of the students from shortest to tallest form ");
	for(i=0;i<n;i++)
	{
		printf("%d ",height[i]);
	}
	getch();
}
