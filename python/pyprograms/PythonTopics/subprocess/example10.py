import subprocess

# Run ls & wc
alpha_p  = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)

beta_p   = subprocess.Popen(['wc'], stdin=alpha_p.stdout)

# Wait for children to die
alpha_rc = alpha_p.wait()
beta_rc  = beta_p.wait()

