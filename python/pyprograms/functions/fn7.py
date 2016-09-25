#!/usr/bin/env python
## topic: functions
#  cmd  : clear; python fn7.py

def hotel_cost(nights): # defining function hotel_cost
    #cost is $100 per night
    """cost per night is 100"""
    return 100 * nights

#print hotel_cost.__doc__    
#nights = input("Enter number of nights to stay in the hotel:  ")
#print "hotel cost for %d days is %d" %(nights, hotel_cost(nights)) # invoking fn

print "hotel cost for 2 days is: ", hotel_cost(2)


def plane_ride_cost(city): # defining fn
    if city == "a":
        return 100
    elif city == "b":
        return 200
    elif city == "c":
        return 300
    elif city == "d":
        return 400
        
#city = raw_input("Enter the name of the city 'a,b,c or d':  ")        
#print "plane ride cost for city '%s' is %d " %(city, plane_ride_cost(city))

print "plane ride cost for city 'a' is: ", plane_ride_cost("a")


def rental_car_cost(days): # defining fn
    if days >= 7:
        return days*40 - 50 # 50 dollar discount
    elif days >= 3 and days < 7:
        return days*40 - 20
    else:
        return days*40
        
#days = input("Enter number of days for rental car:  ")
#print "rental car cost for %d days is %d" %(days, rental_car_cost(days))

print "rental car cost for 4 days is:  ", rental_car_cost(4)


def total_cost(city,days):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)

print    
city = raw_input("Enter the name of the city 'a,b,c or d':   ")
days = input("Enter the no.  of the days to stay in that city:  ")
print "\ntotal cost for city '%s' staying %d days is: %d " % (city,days, total_cost(city, days) )

#    
#print "total cost is: ", total_cost("a", 4)
print


