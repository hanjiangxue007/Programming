CC=gcc
CFLAGS=-Wall -O3
DEPS = 

.c.o: 
	$(CC) -c -o $@ $< $(CFLAGS)

%.out: %.o
	$(CC) -O3 -o $@ $^

all: mandelbrot.out