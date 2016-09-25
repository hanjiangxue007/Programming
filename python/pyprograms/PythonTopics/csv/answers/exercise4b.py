#!/usr/bin/python3

import csv

input_file = open('weird2.csv', 'r', newline='')

data = csv.reader(input_file, delimiter=';')

for line in data:
    [name, birth, death] = line
    print(name+': born', str(birth)+', died', death)
del name, birth, death, line

del data

input_file.close()
del input_file
