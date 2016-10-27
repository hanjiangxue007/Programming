/* Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
 * Date        : Sep 20, 2016
 * Last update :
 *
 * Compile     : gcc -Wall a.c -lm
 * Run         :
 *
 *
 * Inputs      : 1.
 *
 *
 * Outputs     : 1.
 *
 * Info        :
 *
 */

#include<stdio.h>

int main()
{
	FILE *ptr_file;
	char buf[1000];

	ptr_file =fopen("output.txt","r");
	if (!ptr_file)
		return 1;

	while (fgets(buf,1000, ptr_file)!=NULL)
		printf("%s",buf);

	fclose(ptr_file);
	return 0;
}


// Note:The printf statement does not have the new-line (\n) in the format string.
// This is not necessary because the library function fgets adds the \n to
// the end of each line it reads.
