# Author  : Bhishan Poudel
# Date    : Mar 14, 2016


filename="out.txt"
myfile = open(filename,"w")
string = "my name is bhishan poudel"
myfile.write(string)
myfile.close()
print "look inside out.txt"
