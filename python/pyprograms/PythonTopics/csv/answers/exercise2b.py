#!/usr/bin/python3

import csv

input_file = open('produce1.csv', 'r', newline='')

data = csv.reader(input_file)

for line in data:
    item = line[0]

    sum = 0
    for value in line[1:]:
        sum += int(value)
    del value

    print(item+':', sum)

del item, sum, line

del data

input_file.close()
del input_file
