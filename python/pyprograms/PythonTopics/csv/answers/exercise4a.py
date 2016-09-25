#!/usr/bin/python3

import csv

input_file = open('data3.csv', 'r', newline='')

data = csv.reader(input_file, delimiter=' ', skipinitialspace=True)

for line in data:
    [name, birth, death] = line
    print(name, 'was born in', birth, 'and died in', death)
del name, birth, death, line

del data

input_file.close()
del input_file
