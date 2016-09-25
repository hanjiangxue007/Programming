/* Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
 * Date        : Sep 20, 2016
 * Last update :
 *
 * Compile     : gcc -Wall a.c -lm
 * Run         :
 */


#include <stdio.h>
#include <stdlib.h>

int main(void) {

    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t linelen;

    fp = fopen("input.txt", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((linelen = getline(&line, &len, fp)) != -1) {
        printf("\nRetrieved line of length %zu :\n", linelen);
        printf("Contents of the line is: %s", line);
     }

    free(line);
    exit(EXIT_SUCCESS);
}
