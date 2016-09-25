#!/usr/bin/python3

import csv

# Modify this script so that it gets its data from the file weird6.csv.
input_file = open('weird6.csv', 'r', newline='')

data = csv.reader(input_file, delimiter='\t', quotechar="'")

for line in data:
    [name, birth, death] = line
    print(name, 'was born in', birth, 'and died in', death)
del name, birth, death, line

del data

input_file.close()
del input_file
