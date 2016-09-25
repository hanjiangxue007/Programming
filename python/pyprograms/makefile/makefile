# Author  : Bhishan Poudel
# Date    : Feb 20,2016

# Variables
PROGRAM = hello.py

# Execute the program
exec: compile
	python $(PROGRAM)

compile: hello.py
	clear
	echo "Author : Bhishan Poudel"

# Note: if I use terminal command clear, it will show error:
#       TERM environment variable not set

# eg
#compile: hello.py
#	clear


