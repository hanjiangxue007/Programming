# Author    : Bhishan Poudel
# Date      : Mar 14, 2016
# To delete : rm {0..4}.txt

# python -m timeit 'import filewrite_for_loop'

import time

start = time.time()
for x in xrange(0,22):
    filename = str(x)+".txt"
    print(filename)
    myfile = open(filename,"w")
    string = "This is file "+str(x)+".txt"
    myfile.write(string)
    myfile.close()

end = time.time()
print (end - start)
