import os
for dpath, dnames, fnames in os.walk('/home/bhishan/Copy/Programming/Python/pyprograms/rename'):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('IMG_'):
            os.rename(f, f.replace('IMG_', 'bhishan'))
            

#terminal command: rename -v 's/IMG_(\d{4})\.JPG$/bhishan_$1\.jpg/' *.JPG
