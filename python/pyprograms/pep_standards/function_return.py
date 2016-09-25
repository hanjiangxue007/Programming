#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 10, 2016
# Last update :
#





##==============================================================================
## Returning more than one variable type from function call
## answer to life the universe and everything is 42
##==============================================================================
# anti pattern (have to check what function will return)
def get_secret_code(password):
    if password != "bicycle":
        return None
    else:
        return "42"

secret_code = get_secret_code("unicycle")

if secret_code is None:
    print("Wrong password.")
else:
    print("The secret code is {}".format(secret_code))


##==============================================================================
# best practice
def get_secret_code(password):
    if password != "bicycle":
        raise ValueError
    else:
        return "42"


 if used only this line we will get value error
 secret_code = get_secret_code("unicycle")
 this above line is just for checking

try:
    secret_code = get_secret_code("unicycle")
    print("The secret code is {}".format(secret_code))
except ValueError:
    print("Wrong password.")



