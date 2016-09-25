import re
import sys

pattern = r'\\ in'
regexp = re.compile(pattern)

data = open('exercise05.txt', 'r')

for line in data:
    match = regexp.search(line)
    if match:
        sys.stdout.write(line)
