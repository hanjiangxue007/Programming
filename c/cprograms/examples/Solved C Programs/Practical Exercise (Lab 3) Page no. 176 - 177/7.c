/*7.	Write a program to count the number of words in a text.*/
#include<stdio.h>
#include<conio.h>
main()
{
char msg[100];
int i, w = 0;
puts("Enter one paragraph to count words :\n\n ");
gets(msg);
for(i=0;msg[i]!='\0';i++)
{
if(msg[i] == ' ')//checks spaces for counting words.
w ++;
}
printf("\nThere are %d words",w+1);//the last word do not have space at last hence +1.
getch();
}
