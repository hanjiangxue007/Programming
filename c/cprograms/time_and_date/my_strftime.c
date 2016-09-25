#include <stdio.h>
#include <time.h>

int main ()
{
   time_t rawtime;
   struct tm *info;
   char buffer[80];
   char buffer2[80];

   time( &rawtime );

   info = localtime( &rawtime );

   strftime(buffer,80,"%x - %I:%M%p", info);
   printf("Formatted date & time : |%s|\n", buffer );  // Formatted date & time : |02/15/16 - 08:41PM|

   strftime(buffer2,80,"%b %d, %Y", info);
   printf("Date : %s\n", buffer2 );  // Date : Feb 15, 2016

   return(0);
}

/*  Specifier 	Replaced By 								Example
    %a 		Abbreviated weekday name 						Sun
    %A 		Full weekday name 							Sunday
    %b 		Abbreviated month name 							Mar
    %B 		Full month name								March
    %c 		Date and time representation 						Sun Aug 19 02:56:02 2012
    %d 		Day of the month (01-31) 						19
    %H 		Hour in 24h format (00-23) 						14
    %I 		Hour in 12h format (01-12) 						05
    %j 		Day of the year (001-366) 						231
    %m 		Month as a decimal number (01-12) 					08
    %M 		Minute (00-59) 								55
    %p 		AM or PM designation 							PM
    %S 		Second (00-61) 								02
    %U 		Week number with the first Sunday as the first day of week one (00-53) 	33
    %w 		Weekday as a decimal number with Sunday as 0 (0-6) 			4
    %W 		Week number with the first Monday as the first day of week one (00-53) 	34
    %x 		Date representation 							08/19/12
    %X 		Time representation 							02:50:06
    %y 		Year, last two digits (00-99) 						01
    %Y 		Year 									2012
    %Z 		Timezone name or abbreviation 						CDT
    %% 		A % sign 								%
*/
