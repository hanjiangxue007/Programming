print("Hello World!")

#  Use Cython to compile your python program into C...
# cython --embed -o hello.c hello.py

# Use GCC to compile hello.c into an executable file called hello...
# gcc -Wall -I/usr/include/python2.7 -lpython2.7  hello.c -o hello

# gcc -Os -I /usr/include/python3.3m -o hello hello.c -lpython3.3m -lpthread -lm -lutil -ldl

# gives error hello.h not found!
