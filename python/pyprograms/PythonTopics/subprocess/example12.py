import subprocess

lines = [
    'Mary had a little lamb',
    'Its fleece as white as snow,',
    'And every where that Mary went',
    'The lamb was sure to go.',
    '',
    'So Mary visited an abbatoir and ate very well that day.'
    ]

wc_proc = subprocess.Popen(['wc'], stdin=subprocess.PIPE)

for line in lines:
    wc_proc.stdin.write(line.encode())

# wc terminates automatically when its input is closed 
# so we can do either:
# wc_proc.terminate()
# or:
wc_proc.stdin.close()
