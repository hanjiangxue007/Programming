import subprocess

collatz_proc = subprocess.Popen(['./collatz'], stdout=subprocess.PIPE)

for counter in range(0,10000):
    line_raw = next(collatz_proc.stdout)
    line_txt = line_raw.decode('UTF-8')

    # Typically we would do something with the line of input 
    # at this point.  All we are doing is reading in the lines.

    # print(line_txt)

collatz_proc.terminate()
