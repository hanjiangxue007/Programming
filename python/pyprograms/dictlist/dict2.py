# dictionaries 2

print
prices = {}
prices['banana'] = 4
prices['apple'] = 2
prices['orange'] = 1.5
prices['pear'] = 3

print "prices: ", prices
print

stock = {
    'banana' : 6,
    'apple' : 0,
    'orange' : 32,
    'pear' :15
    }
print "stocks:", stock
print

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    
print

total = 0
for key in prices:
    print prices[key]*stock[key]
    total += prices[key] * stock[key]
    
print total


#    While you loop through each item of food, only add the price of the item to 
#    total if the item's stock count is greater than zero.
#    If the item is in stock and after you add the price to the total,
#     subtract one from the item's stock count.


def compute_bill(food):
    total = 0
    count = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
        if stock[item] > 0:
            stock[item] -= 1
    return total

print    
print stock



print
