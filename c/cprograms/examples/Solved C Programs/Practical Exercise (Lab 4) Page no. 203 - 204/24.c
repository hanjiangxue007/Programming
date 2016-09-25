/*24)	A college published the entrance result of the successful candidates for the admission in BBA. The symbol no. of the successful candidates are as follows:
12001		12005		12009		12104		12204		12250
12305		12555		12560		12570		12600		12601
Now, make a program to input a symbol no. and your program should find the given symbol no. is in the list or not.*/
#include<stdio.h>
#include<conio.h>
main()
{
	int sn[]={12001,12005,12009,12104,12204,12250,12305,12555,12560,12570,12600,12601};
	int i,x;
	char found;
	printf("\n The list of successful candidates are ");
	for(i=0;i<12;i++)
	{
		printf("\n %d",sn[i]);
	}
	printf("\nEnter the symbol no. which you wnat to search ");
	scanf("%d",&x);
	//code to search
	for(i=0;i<12;i++)
	{
		if(x==sn[i])
		{
			found=1;
			break;
		}
	}
	if(found==1)
	{
		printf("\n Yes, the symbol no. %d is in the list of successful students ",x);
	}
	else
	{
		printf("\n No, the symbol no. %d is not in the list of successful students ",x);
	}
	getch();
}