import subprocess

ls_output_raw = subprocess.check_output(['ls', '-l'])
ls_output_text = ls_output_raw.decode(encoding='UTF-8')

print('Finished running ls.')
print(ls_output_text)

#ls_output_lines = ls_output_text.splitlines()
#print(ls_output_lines)
