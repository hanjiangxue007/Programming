import re
import sys

words = open('/usr/share/dict/words', 'r')

pattern = 'XXXX'

regexp = re.compile(pattern)

for word in words:
    match = regexp.search(word)
    if match:
        sys.stdout.write(word)
