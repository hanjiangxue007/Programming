import re
import sys

pattern = r'XXXX'

regexp = re.compile(pattern)

data = open('messages', 'r')

for line in data:
    match = regexp.search(line)
    if match:
        sys.stdout.write(line)
