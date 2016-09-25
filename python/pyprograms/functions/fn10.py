#!/usr/bin/env python
#author: bhishan poudel
#cmd   : clear; python fn10.py


#defining function cheeseshop
def cheeseshop(kind, *arguments, **keywords):               #arguments = It's very tasty, sir.
    """\nThis function takes arguments and gives result.\n"""
	
    print "Client: Do you have any", kind, "?"  # arguments = It's really very, VERY tasty, sir.
    print "Shopkeeper: I'm sorry, we're all out of", kind   # kind = Hamburger
    for arg in arguments:                                   # keywords are:
        print "Client:",arg                                 # shopkeeper='Michael Palin'
    print "-" * 50                                          # client="John Cleese"
    keys = sorted(keywords.keys())                          # shop="Cheese Shop"
    for kw in keys:
        print kw, ":", keywords[kw]
print cheeseshop.__doc__				# docstring will printed on top of the function

#invoking function cheeseshop

cheeseshop("Hamburger", "It's very tasty, sir.", 	#cheeseshop(kind, *arguments, **keywords)
           "It's very very tasty,sir.",
           "It's really very, VERY tasty, sir.",
           client="John Cleese",                	# kw = client
           shopkeeper='Michael Palin',          	# keywords[kw] = John Cleese
           shop="Cheese Shop Athens",
           date = "July 4, 2015")
           
           
