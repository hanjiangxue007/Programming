/* Bhishan Poudel
 * Feb 16, 2016
 * Program: To print my custom header lines for python program
 *
 * gcc -Wall -o mypy mypy.c
 *
 * echo "$PATH"
 * we get   /opt/local/bin     and others
 * sudo cp mypy /opt/local/bin/
 * ls /opt/local/bin/    we see mypy executable there
 *
 * or, copy it to /usr/bin
 */

#include<stdio.h>
#include <time.h>

int main()
{
   time_t rawtime;
   struct tm *info;
   char buffer[80];

   time( &rawtime );
   info = localtime( &rawtime );


    printf("#!/usr/bin/env python\n");
    printf("# -*- coding: utf-8 -*-\n\n");
    printf("# Author  : Bhishan Poudel\n");

    strftime(buffer,80,"%b %d, %Y", info);
    printf("# Date    : %s\n", buffer );
    printf("\n\n# Imports\n\n");
    return 0;
}
