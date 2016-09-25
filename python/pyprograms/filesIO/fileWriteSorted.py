#!/usr/bin/python

# cmd : clear; python fileWriteSorted.py

# this program will read unsorted names
# from a text file and creates sorted text file

f1 = open('friends.txt', 'r')
friends_list = f1.readlines()
f1.close()

print 'first name is:', friends_list[0]


# sorting the names
friends_list.sort()
print 'first name is: ', friends_list[0]

# writing the sorted names in a new file

f2 = open('sortedfriends.txt', 'w')
for friend in friends_list:
    f2.write(friend)
f2.close()