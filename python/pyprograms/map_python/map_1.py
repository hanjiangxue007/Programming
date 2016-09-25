

# ref    : http://www.python-course.eu/lambda.php

# lambda
f = lambda x, y : x + y
print(f(1,1))


# The map() Function
# map() is a function with two arguments:

# r = map(func, seq)

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)


print(F)
print("")
print(C)



# map() will apply its lambda function to the elements of the argument lists.

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
m1 = map(lambda x,y:x+y, a,b)
print("")
print(m1)
#[18, 14, 14, 14]


m1 = map(lambda x,y,z:x+y+z, a,b,c)
print(m1)
# [17, 10, 19, 23]


m1 = map(lambda x,y,z:x+y-z, a,b,c)
print(m1)
# [19, 18, 9, 5]



# filtering

