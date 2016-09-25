import subprocess

alpha_p  = subprocess.Popen(['ls', '-l', 'alpha'])
beta_p   = subprocess.Popen(['ls', '-l', 'beta'])

alpha_rc = alpha_p.wait()
beta_rc  = beta_p.wait()

