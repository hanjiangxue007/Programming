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
 * Info        : https://www.codingunit.com/c-tutorial-file-io-using-text-files
 *
 */



#include<stdio.h>

int main()
{
	FILE *ptr_file;
	int x;

	ptr_file =fopen("output.txt", "w");

	if (!ptr_file)
		return 1;

	for (x=1; x<=10; x++)
		fprintf(ptr_file,"%d\n", x);

	fclose(ptr_file);

	return  0;
}
