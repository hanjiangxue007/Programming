#!/usr/bin/python

# cmd: clear; python fn11.py

#defining function cheeseshop
def cheeseshop(kind, *arguments, **keywords):               #arguments = It's very tasty, sir.
    print "Client: Do you have any", kind, "?"              # arguments = It's really very, VERY tasty, sir.
    print "Shopkeeper: I'm sorry, we're all out of", kind   # kind = Hamburger
    for arg in arguments:                                   # keywords are:
        print "Client:",arg                                 # shopkeeper='Michael Palin'
    print "-" * 40                                          # client="John Cleese"
    keys = sorted(keywords.keys())                          # sketch="Cheese Shop Sketch"
    for kw in keys:
        print kw, ":", keywords[kw]

#invoking function cheeseshop

cheeseshop("Hamburger", "It's very tasty, sir.", #cheeseshop(kind, *arguments, **keywords)
           "It's very very tasty,sir.",
           "It's really very, VERY tasty, sir.",
           shopkeeper='Michael Palin',          #kw = shopkeeper and keywords[kw] = Michael Palin
           client="John Cleese",                #
           sketch="Cheese Shop Sketch",
           date = "July 4, 2015")
