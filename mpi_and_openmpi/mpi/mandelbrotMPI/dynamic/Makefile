CC=mpicc
CFLAGS=-Wall -O3
DEPS = 

.c.o: 
	$(CC) -c -o $@ $< $(CFLAGS)

%.out: %.o
	$(CC) $(CFLAGS) -o $@ $^

all: mandelbrot.out