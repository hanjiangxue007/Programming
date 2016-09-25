print("Hello World")
print "This is my"
a = "first program"
print a

print "*****************************************"

b = "I am bhishan"
b.split()
b.split("n")
print (b)

print "**************************************"
c = "bhishan".upper()
print c

print "***************************************"
L = [1, "Bhishan", 7, 22.33, 63, 3334]  # example of list
print L[:]  # [1, 'Bhishan', 7, 22.33, 63, 3334]
print L[:2]  # [1, 'Bhishan']
print L[:4]  # [1, 'Bhishan', 7, 22.33]

list("ham")

print "****************************************"

y = []
y.append("ham")

print(y)  # ['ham']

print "***************************************"

"s" in "something"  # console shows True

print "***************************************"

# tuples () are memory efficient but not adjustable compared to list

x = ("sam", 4, 5)
print x

print "***************************************"

# dictionaries or hashtable or map {}

sam = {}
sam["weapon"] = "chainsaw"
sam["health"] = 10

print(sam)  # {'weapon': 'chainsaw', 'health': 10}
print(sam["weapon"])  # chainsaw

del sam["health"]
print (sam) # {'weapon': 'chainsaw'}

print "***************************************"

x = 15

if (x > 6 and x < 10):
    print ("Congrats")

elif (x == 15):
    print ("This is 15")    # This is 15

elif not (4):
    print ("not 6")

else:
    print ("So sad!")

print  "**********************************************"
x = 0
while (x < 10):
    x += 1

    if (x == 5): break

print x     # 5

print  "**********************************************"
x, y = 0, 0
while (True):
    x += 1
    y += 2
    if (x + y > 10):
        break
    print x, y      # 1 2     2 4     3 6
print "if we indent we get different answer"
print x,y           # 4 8

print  "**********************************************"
x = [1, 2, 7] # list
for i in x:
    print i         # 1 2 7
                    # if we do not indent it will not work
print  "**********************************************"
for i in range(2):
    print i         # 0 1

print  "**********************************************"
for i in range(10, 16, 2):
    print i                 # 10 12 14

print  "**********************************************"
print "not divisible by 3"
for i in range(5):
    if not (i % 3):
        continue
    print i     # 1 2 4
                # print i is just below if not
print  "**********************************************"

fiboSeq = []
a, b = 0, 1
while (b < 3):
    fiboSeq.append(a)
    a, b = b, a + b  # we cannot indent this line
    print fiboSeq  # [0] [0, 1] [0, 1, 1]
print "answer depend on indentation of print"
print fiboSeq      #[ 0, 1, 1]

print  "**********************************************"
factorial = 1
for i in range(1, 4):
    factorial *= i
print factorial     # 6

print  "**********************************************"
primes = []
for i in range(2, 10):
    for x in range(2, i):
        if (i % x == 0):  # 3%2 == 1 3%3 == 0
            break
    else:
        primes.append(i)
       #print primes
print primes            # [2, 3, 5, 7]

print  "**********************************************"
print "now we will study exceptions handling"
# x = 5 + "bag"
# print x

try:
    x = 5 + "bag"
except:
    print "error of adding number and string"

print  "**********************************************"
print "now we will study pass"
y = 5
try:
    y = 6 + "sam"
except:
    pass

print y

print  "**********************************************"
print "now we will study raise" \
      ""
raise TypeError("youGotTypingError")
z = 6 + "sam"
print z

print  "**********************************************"
print "error finally"
try:
    x = 5 + "sam"
except ZeroDivisionError:
    print "will not see this"
finally:
    print "the final word"