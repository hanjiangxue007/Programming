import subprocess

ls_output = open('ls_out.txt', 'w')

rc = subprocess.call(['ls', '-l'], stdout=ls_output)
print('RC = {:d}'.format(rc))

ls_output.close()
