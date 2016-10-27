/* L-7 MCS 572 Wed 7 Sep 2016 mandelbrot.c
 * This program creates the file "mandelbrot.ps", a postscript file
 * with an image of the Mandelbrot set. */

#include <stdio.h>
#include <stdlib.h>

#define XOFFSET 54
#define YOFFSET 288
#define SCALE 432

int iterate ( double x, double y );
/*
 * Returns the number of iterations for z^2 + c 
 * to grow larger than 2, for c = x + i*y, 
 * where i = sqrt(-1), starting at z = 0. */

void write_postscript_plot
 ( FILE *f, int rows, int columns,
   double a, double b, double c, double d, int v );
/*
 * Writes a plot of a Mandelbrot set to the file in postscript format.
 * The plot is generated as a matrix of grayscales with the specified
 * number of rows and columns and written directly into the file.
 * To save toner for the default plot, the grayscales are inverted.
 *
 * The input parameters have the following meaning:
 *   f        pointer to a file which must be opened for writing;
 *   rows     horizontal resolution of the plot;
 *   columns  vertical resolution of the plot as a matrix of gray scales;
 *   a        start of the range for the real part of z = x + i*y;
 *   b        end of the range for the real part of z = x + i*y;
 *   c        start of the range for the imaginary part of z = x + i*y;
 *   d        end of the range for the imaginary part of z = x + i*y;
 *   v        indicates if computation is verbose if v equals 1. */

int main ( int argc, char* argv[] )
{
   int interactive = 0; /* set to 1 for interactive version */
   int verbose = 0;     /* if 1, then more diagnostics */
   int rows,columns;
   double a,b,c,d;
   char filename[80];
   FILE *outputfile;

   if(interactive==1)
   {
      printf("Give the number of rows : "); scanf("%d",&rows);
      printf("Give the number of columns : "); scanf("%d",&columns);
      printf("Give the lower bound for x : "); scanf("%lf",&a);
      printf("Give the upper bound for x : "); scanf("%lf",&b);
      printf("Give the lower bound for y : "); scanf("%lf",&c);
      printf("Give the upper bound for y : "); scanf("%lf",&d);
      printf("Give the name of the output file : "); scanf("%s",filename);
      outputfile = fopen(filename,"w");
      printf("See the file %s for results...\n",filename);
   }
   else
   {
      rows = 500; columns = 500;
      a = -2.0; b = 2.0; c = -2.0; d = 2.0;
      outputfile = fopen("mandelbrot.ps","w");
   }
   write_postscript_plot(outputfile,rows,columns,a,b,c,d,verbose);
   fclose(outputfile);

   return 0;
}

void write_postscript_plot
 ( FILE *f, int rows, int columns,
   double a, double b, double c, double d, int v )
{
   int i,j,n;
   double x,y;
   double dx = (b-a)/(columns-1);
   double dy = (d-c)/(rows-1);

   fprintf(f,"%%!PS\n");
   fprintf(f,"%%%%BoundingBox: 0 300 500 720\n");
   fprintf(f,"/picstr %d string def\n",rows);
   fprintf(f,"%d %d translate\n",XOFFSET,YOFFSET);
   fprintf(f,"%d %d scale\n",SCALE,SCALE);
   fprintf(f,"%d %d %d\n",rows,columns,8);
   fprintf(f,"[%d 0 0 -%d 0 %d]\n",rows,columns,columns);
   fprintf(f,"{currentfile picstr readhexstring pop}\n");
   fprintf(f,"image\n");
   if(v == 0)
      for(i=0,y=d; i<rows; i++,y-=dy,fprintf(f,"\n"))
         for(j=0,x=a; j<columns; j++,x+=dx)
	   {
	     fprintf(f,"%.2x",255-iterate(x,y)); /* inverted grayscale */
	     //printf("x,y,z: %f,%f,%i\n",x,y,iterate(x,y));
	   }
   else
   {
      int nbit,totit = 0;

      for(i=0,y=d; i<rows; i++,y-=dy,fprintf(f,"\n"))
         for(j=0,x=a; j<columns; j++,x+=dx)
         {
            nbit = iterate(x,y);
            fprintf(f,"%.2x",255-nbit); /* inverted grayscale */
            totit = totit + nbit;
         }
      printf("Total number of iterations : %d\n",totit);
   }
   fprintf(f,"showpage\n");
}

int iterate ( double x, double y )
{
   double wx,wy,v,xx;
   int k = 0;

   wx = 0.0; wy = 0.0; v = 0.0;
   while ((v < 4) && (k++ < 254))
   {
      xx = wx*wx - wy*wy;
      wy = 2.0*wx*wy;
      wx = xx + x;
      wy = wy + y;
      v = wx*wx + wy*wy; 
   }

   return k;
}
