import subprocess

filename = 'interchange.dat'

# Run ls
output_file = open(filename, 'w')
alpha_p  = subprocess.Popen(['ls', '-l'], stdout=output_file)
alpha_rc = alpha_p.wait()
output_file.close()

# Run wc
input_file = open(filename, 'r')
beta_p   = subprocess.Popen(['wc'], stdin=input_file)
beta_rc  = beta_p.wait()
input_file.close()

