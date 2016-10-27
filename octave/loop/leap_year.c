/* Author    : Bhishan Poudel
 * Date      : May 25, 2016
 */

#include <stdio.h>

// function to calculate leap year
int is_leap_year(int year)
{
    return (  (!(year % 4) && (year % 100)) || (!(year % 400))  ) ? 1 : 0;
}


// main function
int main()
{
    // declare variables
    int test_case[] = {1900, 1994, 1996, 1997, 2000}, key, end, year;

    // describe leap year
    printf("This program determines whether the given year is leap year or not\n");
    printf("The year is leap year if it is divisible by 4 in general.\n");
    printf("But, in some rare cases it is not true.\n");
    printf("If the year is divisible by 100 (century year), then it is\n");
    printf("leap year if only it is divisible by 400.\n");
    printf("For example, 2000 is leap year, but not 2100,2200,1700.\n\n");


    // use leap year function
    for (key = 0, end = sizeof(test_case)/sizeof(test_case[0]); key < end; ++key) {
        year = test_case[key];
        printf("%d is %sa leap year.\n", year, (is_leap_year(year) == 1 ? "" : "not "));
    }


    // description of the function
    printf("\ndescription of the function\n");

    printf("In C and operator && has higher precedence than or || \n\n");
    printf("AND gives 1 if both values are 1, otherwise 0.\n");
    printf("1 && 1 = %d\n", 1&&1);
    printf("1 && 0 = %d\n", 1&&0);
    printf("0 && 0 = %d\n\n", 1&&0);


    printf("OR gives 0 if both values are 0, otherwise 1.\n");
    printf("1 || 1 = %d\n", 1||1);
    printf("1 || 0 = %d\n", 1||0);
    printf("0 || 0 = %d\n\n", 0||0);

    int logic;
    logic = (2000 % 4);  // 0 is the remainder, divisible
    printf("(2000 %% 4) = %d\n", logic);

    logic = !(2000 % 4);  // 1
    printf("!(2000 %% 4) = %d\n", logic);

    logic = (2000 % 100); // 0
    printf("(2000 %% 100) = %d\n", logic);

    logic = (!(2000 % 4)) && (2000 % 100) ; // 1 && 0 = 0, and 1 only when both 1
    printf("(!(2000 %% 4)) && (2000 % 100) = %d\n", logic);

    logic = (!(2000 % 400)); // 1
    printf("(!(2000 %% 400)) = %d\n", logic);

    logic = (!(2000 % 4) && (2000 % 100)) || (!(2000 % 400));
    printf("(!(2000 %% 4) && (2000 % 100)) || (!(2000 % 400)) = %d\n", logic);

    printf("\n\n!(year %% 4)  means years not divisible by 4.\n");
    printf("(year %% 100) means years divisible by 100.\n\n");











    return 0;
}
