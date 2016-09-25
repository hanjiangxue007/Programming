# python important.py 

# ref: http://stackoverflow.com/questions/419163/what-does-if-name-main-do

# this is a script which i will use as a module (boilerplate code) in another python program

def do_important():
    '''This function does something very important'''
    print 'This is an important function'
    


# calling this function
#do_important()

# Note: If we uncomment this, whenever we use this module 'important.py' this function
#   will also be called automatically. so we use _main_ here. 


if __name__ == "__main__":
    do_important()
    

## better way
## define the main function here, so that we can import it later

#def main():
#    '''business logic for when running this module as the primary one!'''
#    setup()
#    foo = do_important()
#    bar = do_even_more_important(foo)
#    for baz in bar:
#        do_super_important(baz)
#    teardown()

## Here's our payoff idiom!
#if __name__ == '__main__':
#    main()
