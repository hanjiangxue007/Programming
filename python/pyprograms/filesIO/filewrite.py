# topic: file write

#example 1

myfile = open("out.txt","w")
string = "my name is bhishan poudel"
myfile.write(string)
myfile.close()
print "look inside out.txt"

#example 2

principal   = 100
rate        = 0.10  # 10%
numyears    = 5
year        = 1

myfile2 = open("out2.txt","w")
str2 = "year\tprincipal\n"
myfile2.write(str2)

while  year <= numyears:
    principal = principal * (1 + rate)
    myfile2.write("%d: \t%0.2f\n" % (year,principal))
    year +=1
myfile2.close()

print "look inside out2.txt"
