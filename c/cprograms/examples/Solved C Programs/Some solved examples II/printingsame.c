//Quine By St0le!
 #include<stdio.h>
 #include<conio.h>
char *p="#include %c%c char *p=%c%s%c; %c%c void main(){%c%c printf(p,13,10,34,p,34,13,10,13,10,13,10,13,10); %c%c }";
void main(){
printf(p,13,10,34,p,34,13,10,13,10,13,10,13,10);
getch();
 }

