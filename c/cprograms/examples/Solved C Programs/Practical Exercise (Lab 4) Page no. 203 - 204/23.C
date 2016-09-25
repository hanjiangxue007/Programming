/*23)	Write a program to input mobile number of any 50 students in a class.
 Then, ask the user to input a mobile number and find it is in the contact list or not.*/
 #include<stdio.h>
 #include<conio.h>
 #include<string.h>
 main()
 {
	char mobileno[50][10],srchmobile[10],result;
	int i;
	printf("Enter the mobile no. of any 50 students ");
	for(i=0;i<50;i++)
	{
		gets(mobileno[i]);
	}
	printf("Enter the mobile no. which you want to search ");
	gets(srchmobile);
	//code to search
	for(i=0;i<50;i++)
	{
		if(strcmpi(srchmobile,mobileno[i])==0)
		{
			result='y';
			break;
		}
	}
	if(result=='y')
	{
		printf("\n Yes, the mobile no. which you are searching is in the list ");
	}
	else
	{
		printf("\n No, the mobile no. which you are searching is not in the list ");
	}
	getch();
	return(0);
}
