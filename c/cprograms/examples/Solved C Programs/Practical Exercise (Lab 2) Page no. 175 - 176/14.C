/*14.	Write a program to input the cost price and selling price and calculate the profit or loss.*/
#include<stdio.h>
#include<conio.h>
main()
{
	float cp,sp,amt;
	printf("Enter the cost price of the item ");
	scanf("%f",&cp);
	printf("Enter the sales price of the item ");
	scanf("%f",&sp);
	if(sp>cp)
	{
		amt=sp-cp;
		printf("\n The profit amount=Rs.%.2f",amt);
	}
	else if(cp>sp)
	{
		amt=cp-sp;
		printf("\n The loss amount=Rs.%.2f",amt);
	}
	else
	{
		printf("\n There is neither profit nor loss");
	}
	getch();
	return(0);
}
