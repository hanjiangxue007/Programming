#list examples
# source: http://effbot.org/zone/python-list.htm

L = [10,20,30]

#example 1: printing list items
for item in L:
        print item * 2
        
# If you need both the index and the item, use the enumerate function:
print"\nindex,item in enumerate(L)"
for index, item in enumerate(L):
        print index, item
        
# If you need only the index, use range and len: 
print "\nrange(len(L))"
for index in range(len(L)):
        print index
        
# The list object supports the iterator protocol
print("\niteration")
i = iter(L)
item = i.next() # fetch first value
item = i.next() # fetch second value
item = i.next() # fetch second value
