#!/usr/bin/python


#fucntions in Python
#cmd : clear; python fn1.py

#function 1
def happyBirthdayBhishan(): #function declaration
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Bhishan.")
    print("Happy Birthday to you!")

happyBirthdayBhishan()        # function invocation
print "*****************************************"

#function 2
def happyBirthday(person):          # person  is function argument or paramater
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

happyBirthday("Bhishan")
print "*"*40

print
happyBirthday('Bhishan')

print "*"*40
person = raw_input("Enter the name of the person:  ")
happyBirthday(person)

print "****************************************\n"










