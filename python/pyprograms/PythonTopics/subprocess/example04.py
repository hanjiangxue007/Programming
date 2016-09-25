import subprocess

wc_input = open('treasure.txt', 'r')

rc = subprocess.call(['wc'], stdin=wc_input)
print('RC = {:d}'.format(rc))

wc_input.close()


# wc prints following:
# numbers of lines, words and characters
