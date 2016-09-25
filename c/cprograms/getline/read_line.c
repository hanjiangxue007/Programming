/* Author      : Bhishan Poudel; Physics PhD Student, Ohio University
 * Date        : Sep 17, 2016
 * Last update :
 *
 * Compile     : gcc -Wall -O3 -o a a.c -lm -lcfitsio -lpthread -lfftw3f
 * Run         :
 *
 *
 */

#include <stdio.h>
#include <stdlib.h>

int main()
{
        char    *buffer;
        int     memory_read;
        size_t  n = 1024;

        // allocate memory for buffer
        buffer = malloc(n+1);

        // type a line in stdin
        puts("Enter stream, or line of text, here: ");

        // read buffer along with memory read
        memory_read =  getline(&buffer, &n, stdin);

        //print buffer
        if (memory_read == -1) {
            printf("Error: only EOF without text read\n"); }

        else {
            printf("You typed: %s\n", buffer); }


        // always free the memory
        free(buffer);




return 0; }

//if (memory_read == -1)

//{

//puts (“Error : only EOF without text read”);

//}

//else

//{

//puts (your_string);

//}
