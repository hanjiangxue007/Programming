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
 * Info        : http://stackoverflow.com/questions/9206091/going-through-a-text-file-line-by-line-in-c
 *
 */

#include <stdio.h>

int main(int argc, char* argv[])
{
    //char const* const fileName = argv[1]; /* should check that argc > 1 */

    char const* const fileName = 'input.txt'
    FILE* file = fopen(fileName, "r"); /* should check the result */
    char line[256];

    while (fgets(line, sizeof(line), file)) {
        /* note that fgets don't strip the terminating \n, checking its
           presence would allow to handle lines longer that sizeof(line) */
        printf("%s", line); 
    }
    /* may check feof here to make a difference between eof and io failure -- network
       timeout for instance */

    fclose(file);

    return 0;
}


// Note:The printf statement does not have the new-line (\n) in the format string.
// This is not necessary because the library function fgets adds the \n to
// the end of each line it reads.
