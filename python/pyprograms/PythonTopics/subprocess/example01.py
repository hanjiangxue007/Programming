import subprocess


print('About to run ls.')
subprocess.call(['ls', '-l'])
print('Finished running ls.')
