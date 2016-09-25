#!/usr/bin/python3

import csv

input_file = open('produce2.csv', 'r', newline='')

data = csv.reader(input_file, delimiter=' ', skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)

for line in data:
    item = line[0]

    multiplier = line[1]

    sum = 0
    for value in line[2:]:
        sum += int(value)
    del value

    print(item+':', multiplier*sum)

del item, multiplier, sum, line

del data

input_file.close()
del input_file
