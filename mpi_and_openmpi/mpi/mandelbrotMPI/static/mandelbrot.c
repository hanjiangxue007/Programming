/* L-7 MCS 572 Wed 7 Sep 2016 mandelbrot.c
 * This program creates the file "mandelbrot.ps", a postscript file
 * with an image of the Mandelbrot set.
 * Code amended to run using MPI in a static load balancing configuration 
 * for HW2 -Martin Graham */

#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

#define tag 100
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
   double a, double b, double c, double d, int v,int p);
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
int manager(FILE * f,double a,double b,double c, double d,int rows,int columns,int p);

int worker(int i,int (*f)(double x,double y));

int main ( int argc, char* argv[] )
{
   int p,myid;
   MPI_Init(&argc,&argv);
   MPI_Comm_size(MPI_COMM_WORLD,&p);
   MPI_Comm_rank(MPI_COMM_WORLD,&myid);
   
   if(myid==0)
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
	   //	   outputfile = fopen(filename,"w");
	   printf("See the file %s for results...\n",filename);
	 }
       else
	 {
	   rows = 500; columns = 500;//5000
	   a = -2.0; b = 2.0; c = -2.0; d = 2.0;
	   outputfile = fopen("mandelbrot.ps","w");
	   
	 }
       write_postscript_plot(outputfile,rows,columns,a,b,c,d,verbose,p);
       fclose(outputfile);
       //       printf("test\n");
     }
   else worker(myid,iterate);
   
   MPI_Finalize();
   return 0;
}

void write_postscript_plot
 ( FILE *f, int rows, int columns,
   double a, double b, double c, double d, int v ,int p)
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
   if(v == 0)     manager(f,a,b,c,d,rows,columns,p);
      /* for(i=0,y=d; i<rows; i++,y-=dy,fprintf(f,"\n")) */
      /*    for(j=0,x=a; j<columns; j++,x+=dx) */
      /*       fprintf(f,"%.2x",255-iterate(x,y)); /\* inverted grayscale *\/ */
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

int manager(FILE * f,double a,double b,double c, double d,int rows,int columns,int p)
{

  double x,y;
  //  FILE * test=fopen("outfile.ps","w");
  double dx = (b-a)/(columns-1);
  double dy = (d-c)/(rows-1);
  printf("Rows: %i, columns: %i\n",rows,columns);
  int * values;
  int k;
  values=calloc(rows*columns,sizeof(int));

  int job=-1;
  int j;
  do
    {
      for(j=1;j<p;j++)
	{
	  job++;
	  if(job>=rows*columns) break;
	  x=a+dx*(job/rows);
	  y=d-dy*(job%rows);
	  int d=1+(job)%(p-1);
	  MPI_Send(&job,1,MPI_INT,j,tag,MPI_COMM_WORLD);
	  MPI_Send(&x,1,MPI_DOUBLE,j,tag,MPI_COMM_WORLD);
	  MPI_Send(&y,1,MPI_DOUBLE,j,tag,MPI_COMM_WORLD);	    	      
	}
      if(job>=rows*columns)
	{

	  break;
	}
      for(j=1;j<p;j++)
	{

	  MPI_Status status;
	  MPI_Recv(&job,1,MPI_INT,j,tag,MPI_COMM_WORLD,&status);
	  MPI_Recv(&values[job],1,MPI_INT,j,tag,MPI_COMM_WORLD,&status);
	}
    } while(job<columns*rows);
  
  job=-1;
  for(j=1;j<p;j++)
    {
      MPI_Send(&job,1,MPI_INT,j,tag,MPI_COMM_WORLD);
    }
  int i;
  for(i=0,y=d;i<rows;i++,y-=dy,fprintf(f,"\n"))
    for(j=0,x=a;j<columns;j++,x+=dx)
      {
	int ind=i*rows+j;
	fprintf(f,"%.2x",255-values[ind]); /* inverted grayscale */
      }
  free(values);
  return 0;
}

int worker(int i,int (*f)(double x,double y))
{
  int myjob,k;
  double x,y;
  MPI_Status status;
  printf("Hello from %i\n",i);
  do
    {
      MPI_Recv(&myjob,1,MPI_INT,0,tag,MPI_COMM_WORLD,&status);
      if (myjob==-1) break;

      MPI_Recv(&x,1,MPI_DOUBLE,0,tag,MPI_COMM_WORLD,&status);
      MPI_Recv(&y,1,MPI_DOUBLE,0,tag,MPI_COMM_WORLD,&status);
      k=f(x,y);
      MPI_Send(&myjob,1,MPI_INT,0,tag,MPI_COMM_WORLD);
      MPI_Send(&k,1,MPI_INT,0,tag,MPI_COMM_WORLD);
    }
  while(myjob!=-1);
  printf("Goodbye from %i\n",i);
  return 0;
}
