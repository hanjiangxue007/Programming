# Write your function below!
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
    return count
mylist= ["fizz","cat","fizz"]  
 
print fizz_count(["fizz","cat","fizz"])
print fizz_count(mylist)
