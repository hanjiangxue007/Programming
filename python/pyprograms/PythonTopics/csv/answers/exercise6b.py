#!/usr/bin/python3

import csv

input_file = open('produce2.csv', 'r', newline='')
output_file = open('produce2.out', 'w', newline='')

data_in = csv.reader(input_file, delimiter=' ', skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
data_out = csv.writer(output_file, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL)

for line in data_in:
    item = line[0]

    multiplier = line[1]

    sum = 0
    for value in line[2:]:
        sum += int(value)
    del value

    calc = multiplier*sum

    print(item+':', calc)
    data_out.writerow([item, sum, calc])

del item, multiplier, sum, calc, line

del data_in
del data_out

input_file.close()
output_file.close()
del input_file, output_file
