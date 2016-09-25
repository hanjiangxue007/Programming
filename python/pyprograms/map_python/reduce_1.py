

# ref    : http://www.python-course.eu/lambda.php

# Reducing a List
# The function reduce(func, seq) continually applies the
# function func() to the sequence seq. It returns a single value.

val1 = reduce(lambda x,y: x+y, [47,11,42,13])
print(val1)
# 47+11=58, then 58+42=100, then 100+13=113
#113 


# Determining the maximum of a list of numerical values by using reduce:
f = lambda a,b: a if (a > b) else b
max_value =  reduce(f, [47,11,42,102,13])
print(max_value)
# 102

# Calculating the sum of the numbers from 1 to 100:
sum1 = reduce(lambda x, y: x+y, range(1,101))
print(sum1)
#5050

