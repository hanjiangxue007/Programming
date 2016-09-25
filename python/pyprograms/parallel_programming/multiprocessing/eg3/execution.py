import subprocess


def run_main_with_args(filename,name,today,dbfolder):
    print('{} {} {}'.format('\nfilename: ',filename, ''))
    print('{} {} {}'.format('name: ',name, ''))
    print('{} {} {}'.format('today: ',today, ''))
    print('{} {} {}'.format('dbfolder: ',dbfolder, ''))

    outfile = dbfolder+ '/' + name + '.txt'
    with open (outfile, 'w') as fout:
        print('name', file=fout)
