import subprocess

ls_output = open('ls_out.txt', 'w')

alpha_rc = subprocess.call(['ls', '-l', 'alpha'])
beta_rc  = subprocess.call(['ls', '-l', 'beta'])

ls_output.close()
