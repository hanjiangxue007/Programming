/*3.	Write a C program to swap two values by using function.*/
#include<stdio.h>
#include<conio.h>
void swap(int *,int *);
main()
{
	int x,y;
	printf("Enter the first number : ");
	scanf("%d",&x);
	printf("Enter the second number : ");
	scanf("%d",&y);
	printf("\nThe value of x before swapping =%d ",x);
	printf("\nThe value of y before swapping=%d",y);
	//code to call function
	swap(&x,&y);
	printf("\nThe value of x after swapping =%d ",x);
	printf("\nThe value of y after swapping=%d",y);
	getch();
}
void swap(int *a,int *b)
{
	int t;
	t=*a;
	*a=*b;
	*b=t;
}
