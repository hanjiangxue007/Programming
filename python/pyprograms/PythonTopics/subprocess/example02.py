import subprocess

# method 1
#print('About to run ls.')
#rc = subprocess.call(['ls', '-l'])
#print('Finished running ls.')


# method 2
with open('ls_out.txt', 'w') as ls_output:
    rc = subprocess.call(['ls', '-l'], stdout=ls_output)

print('RC = {:d}'.format(rc))
