import re
import sys

pattern = 'Fred'
regexp = re.compile(pattern)

for line in sys.stdin:
    match = regexp.search(line)
    if match:
        sys.stdout.write(line)
